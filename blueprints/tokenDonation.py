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
        isMentor = userData[7]
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
        isMentor = userData[7]
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
        # Inheriting classes
        accountRepository = AccountRepository()
        entitiesRepository = EntitiesRepository()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Ensuring the user is a mentor before loading information into the modal
        userData = accountRepository.getWithID(userID)
        isMentor = userData[7]
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
        communityChosen = data["community"]
        tokensToDonate = int(data["amount"])

        # Inheriting classes
        accountRepository = AccountRepository()
        entitiesRepository = EntitiesRepository()
        tokensRepository = TokensRepository()
        transactionsRepository = TransactionsRepository()
        uploads = Uploads()
        email = Email()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Ensuring the user is a mentor before loading information into the modal and getting their email
        userData = accountRepository.getWithID(userID)
        isMentor = userData[7]
        if isMentor is not None:
            if isMentor == 1:
                userEmail = userData[3]
                # Ensures community exists
                entities = entitiesRepository.getWithEntityID(communityChosen)
                entityName = entities[0][1]
                if entities is not None:
                    # Gets all the data about tokens that are related to the current user
                    tokensData = tokensRepository.getWithUserID(userID)
                    # Gets the number of tokens the user currently has
                    tokenCounter = 0
                    for _ in tokensData:
                        tokenCounter += 1

                    # Ensures the user has enough tokens
                    if tokensToDonate > tokenCounter:
                        email.send(
                        "Transaction Faliure",f"You have attempted to donate more tokens than you own, your our Token balance is {tokenCounter}.", userEmail)
                        return "Invalid input from user", 406

                    # Carries out the transaction for each token for as many tokens as they want to donate
                    for token in range(tokensToDonate):
                        if tokenCounter > 0:
                            currentTokenID = tokensData[token][0]
                            currentTokenCreated = tokensData[token][3]
                            # Carrying out the transaction for the Token
                            transactionsRepository.createTransactionLog(currentTokenID, userID, False, communityChosen, True, True, currentTokenCreated)

                            # Updating the Tokens OwnerID
                            tokensRepository.updateOwnerID(communityChosen, currentTokenID)

                            tokenCounter -= 1

                    # Sends email to user following the transaction
                    email.send("Transaction Transcript", f"You have successfully donated {tokensToDonate} Tokens to {entityName}. Your Token balance is {tokenCounter}.", userEmail)

                    # Return a success message
                    return "Token(s) Donated successfully", 200
            # Return a error message if user is not a moderator
            return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401