from flask import Blueprint, render_template, request, redirect, session
from datetime import datetime
import json
import os

from data.accountRepository import AccountRepository
from data.entitiesRepository import EntitiesRepository
from data.tokensRepository import TokensRepository
from data.transactionsRepository import TransactionsRepository
from logic.uploads import Uploads
from models.footerModel import FooterModel
from models.headerModel import HeaderModel
from logic.email import Email


mentorDonation = Blueprint("mentorDonation", __name__)

@mentorDonation.route('/community/approved/donate')
def mentor_Donation():
    if "UserID" in session:
        # Inheriting classes
        accountRepository = AccountRepository()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Ensuring the user is a mentor before loading the community donate section
        userData = accountRepository.getWithID(userID)
        isMentor = userData[6]
        if isMentor is not None:
            if isMentor == 1:
                # Renders page
                return render_template('mentorTokenDonation.html', footer=FooterModel.standardFooter(), header=HeaderModel.standardHeader())
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401

@mentorDonation.route('/api/community/approved/donate', methods=['GET'])
def mentor_Donation_view():
    # Ensures the user is logged in
    if 'UserID' in session:

        # Inheriting classes
        accountRepository = AccountRepository()
        entitiesRepository = EntitiesRepository()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Ensuring the user is a mentor before loading the select section
        userData = accountRepository.getWithID(userID)
        isMentor = userData[6]
        if isMentor is not None:
            if isMentor == 1:
                communities = entitiesRepository.getApprovedEntities()
                returnData = []
                if communities is not None:
                    for community in communities:
                        dataTimeStamp = community[7]
                        dataDateTime = datetime.fromtimestamp(dataTimeStamp)
                        #Appends the data in the correct format to the empty list
                        returnData.append({
                            "entityID": community[0],
                            "name": community[1],
                            "description": community[2],
                            "created": dataDateTime.ctime()
                        })
                # Returns the array as a JSON
                return json.dumps(returnData)
        # Return a error message if user is not a moderator
        return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401

@mentorDonation.route('/api/community/approved/donate/selected', methods=['GET'])
def mentor_Donation_view_selected():
    if "UserID" in session:
        selectedEntity = request.args.get("entityID")
        print(selectedEntity)
        # Inheriting classes
        accountRepository = AccountRepository()
        entitiesRepository = EntitiesRepository()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Ensuring the user is a mentor before loading information into the modal
        userData = accountRepository.getWithID(userID)
        isMentor = userData[6]
        if isMentor is not None:
            if isMentor == 1:
                communities = entitiesRepository.getWithEntityID(int(selectedEntity))
                returnData = []
                if communities is not None:
                    for community in communities:
                        isCompany = community[5]
                        # Returns true and false in a more readable format for the mentor
                        if isCompany == 1:
                            isCompany = "Yes"
                        else:
                            isCompany = "No"
                        # Appends the data from the database to the empty list
                        returnData.append({
                            "entityID": community[0],
                            "name": community[1],
                            "description": community[2],
                            "profilePicture": community[3],
                            "profileBanner": community[4],
                            "isCompany": isCompany,
                            "isApproved": community[6]
                        })
                # Returns the array as a JSON
                return json.dumps(returnData)

        # Return a error message if user is not a mentor
        return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401

@mentorDonation.route('/api/community/approved/donate/selected/action', methods=['PUT'])
def get_not_approved_community_Review_descition():
    # Ensures the user is logged in
    if 'UserID' in session:

        # Gets the JSON payload from the request
        data = request.get_json()
        CurrentEntity = data["community"]
        numOfTokens = data["amount"]

        # Inheriting classes
        accountRepository = AccountRepository()
        entitiesRepository = EntitiesRepository()
        tokensRepository = TokensRepository()
        transactionsRepository = TransactionsRepository()
        uploads = Uploads()

        # Ensuring the user is a mentor before loading information into the modal
        userData = accountRepository.getWithID(userID)
        isMentor = userData[6]
        if isMentor is not None:
            if isMentor == 1:
                # Using the EntityID to get the UserID so that we can get the user email
                entities = entitiesRepository.getWithEntityID(CurrentEntity)
                if entities is not None:
                    communityPostUserID = entitiesMembersRepository.GetWithEntity(CurrentEntity)[0]
                    userData = accountRepository.getWithID(int(communityPostUserID))
                    userEmail = userData[3]
                    # Depending on if the community was accepted or rejected, the Sql statment is called and ranusing the EntityID and an email is sent to the user
                    if decision == 1:
                        entitiesRepository.DecisionAccept(CurrentEntity)
                        email.send("Request Accepted","We are pleased to inform you that, your request to create a community was accepted. For inquiries contact us at example@example.co.uk.", userEmail)
                    else:
                        entitiesRepository.DecisionDecline(CurrentEntity)
                        email.send("Request Denied", "We regret to inform you that, your request to create a community was denied. For further information or inquiries contact us at example@example.co.uk.", userEmail)
                    # Return a success message
                    return "Community created successfully", 200
            # Return a error message if user is not a moderator
            return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401