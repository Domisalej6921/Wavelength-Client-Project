from flask import Blueprint, render_template, request, redirect, session
from datetime import datetime
import json
import os
from data.entitiesRepository import EntitiesRepository
from data.entitiesMembersRepository import EntitiesMembersRepository
from data.accountRepository import AccountRepository
from logic.uploads import Uploads
from models.footerModel import FooterModel
from models.headerModel import HeaderModel
from data.sitePermissionsRepository import SitePermissionsRepository
from logic.email import Email


community = Blueprint("community", __name__)

@community.route('/community/create')
def create_community():
    return render_template('createCommunity.html', footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))


# To help me write the following code, I read through one of my team members backend code for creating a POST API route
# The name of the file I learnt from is Registry.py within blueprints
@community.route('/api/community/create', methods=['POST'])
def create_community_form():
    if "UserID" in session:
        # Gets the JSON payload from the request and inherits classes
        data = request.get_json()

        entitiesRepository = EntitiesRepository()
        entitiesMembersRepository = EntitiesMembersRepository()
        accountRepository = AccountRepository()
        uploads = Uploads()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Learnt about HTTP status codes from "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes"
        # The status codes return to the JS file to help the client understand the nature of the issue

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400
        
        # Checks if the JSON has the required fields
        if "name" not in data or "description" not in data or "isCompany" not in data:
            return "The JSON payload is missing required fields!", 400

        if type(data["name"]) is not str or type(data["description"]) is not str or type(data["isCompany"]) is not bool:
            return "The JSON payload has incorrect field types!", 400

        # Checks if the JSON has empty fields for name and description
        if len(data["name"]) == 0 or len(data["description"]) == 0:
            return "The JSON payload contains empty fields!", 400

        # Check if the JSON has the correct field types
        # Learnt about the isdigit method from "https://www.w3schools.com/python/ref_string_isdigit.asp"
        if data['name'].isdigit() or data['description'].isdigit():
            return "The name or description should not exclusively contain numbers!", 406

        # Check that the user is allowed to create a community
        account = accountRepository.getWithID(userID)
        if account[6] == 0:
            return "Your account does not have the required permissions to preform this action!", 403

        # Create community data dictionary
        communityData = {
            "Name": data["name"],
            "Description": data["description"],
            "ProfilePictureID": "",
            "BackgroundID": "",
            "isCompany": data["isCompany"],
            "isApproved": 0,
            "Created": int(datetime.now().timestamp())
        }

        # Check if the profile picture is being changed
        # imageFields = list of tuples: (JSON payload field name, database field name, max size in MB)
        imageFields = [("profilePicture", "ProfilePictureID", 2), ("profileBanner", "BackgroundID", 5)]
        for field, dbField, maxSize in imageFields:
            if data[field] is not None:
                # Validate the image
                imageID, extension, size = uploads.checkImage(data[field])
                # Check if the profile picture is above x MB
                if size > maxSize:
                    uploads.rejectImage(imageID, extension)
                    return f"The picture is too large! Max size is {maxSize}MB", 406
                elif extension not in os.environ["allowedFileExtensions"]:
                    uploads.rejectImage(imageID, extension)
                    return "The picture does not use a valid file extension", 406

                # Otherwise accept and override the image in the dictionary

                uploads.acceptImage(imageID, extension)
                communityData[dbField] = imageID
            else:
                return "The JSON payload is missing required fields!", 400

        # Insert the community into the database
        entitiesRepository.insert(communityData)

        # Get the new community's ID
        communityID = int(entitiesRepository.getIDWithProfilePictureID(communityData["ProfilePictureID"])[0])

        # Insert the user into the community members table
        entitiesMembersRepository.insert({
            "EntityID": communityID,
            "UserID": userID,
            "Role": "Founder",
            "isAdmin": 1,
            "Created": int(datetime.now().timestamp())
        })

        # Return a success message
        return "Community created successfully", 200
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401


@community.route('/community/review')
def review_community():
    # Ensures the user is logged in
    if "UserID" in session:
        # Inherits classes
        sitePermissionsRepository = SitePermissionsRepository()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        # Loads the page if the user has the permissions a moderator would have
        if perms is not None:
            if perms[1] == 1:
                return render_template('communityReview.html', footer=FooterModel.standardFooter(), header=HeaderModel.standardHeader())

        # If the user is not a moderator they are sent vack to the account dashboard
        return redirect('/account/dashboard')
    else:
        # If the user is not logged in they are sent to the login page
        return redirect('/login')

@community.route('/api/community/listNotApproved', methods=['GET'])
def get_not_approved_community():
    # Ensures the user is logged in
    if 'UserID' in session:
        # Inherits classes
        sitePermissionsRepository = SitePermissionsRepository()
        entitiesRepository = EntitiesRepository()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        if perms is not None:
            if perms[1] == 1:
                # Using the EntityID to get the UserID so that we can get the user email
                entities = entitiesRepository.getReviewPageData()
                returnData = []
                if entities is not None:
                    for entity in entities:
                        # Learnt about the datetime and ctime methods from:
                        # "https://docs.python.org/3/library/datetime.html"
                        dataTimeStamp = entity[7]
                        dataDateTime = datetime.fromtimestamp(dataTimeStamp)
                        #Appends the data in the correct format to the empty list
                        returnData.append({
                            "entityID": entity[0],
                            "name": entity[1],
                            "created": dataDateTime.ctime()
                        })
                # Returns the array as a JSON
                return json.dumps(returnData)
        # Return a error message if user is not a moderator
        return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401


@community.route('/api/community/listNotApproved/selected', methods=['GET'])
def get_not_approved_community_Review():
    # Ensures the user is logged in
    if 'UserID' in session:
        # Learnt how to get parameters from URLs from:
        # "https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask/24892131#24892131"
        CurrentEntity = request.args.get("entityID")
        # Inherits classes
        sitePermissionsRepository = SitePermissionsRepository()
        entitiesRepository = EntitiesRepository()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        if perms is not None:
            if perms[1] == 1:
                # Gets data about the Current Entity from the database
                entities = entitiesRepository.getWithEntityID(int(CurrentEntity))
                returnData = []
                if entities is not None:
                    for entity in entities:
                        isCompany = entity[5]
                        # Returns true and false in a more readable format for the moderator
                        if isCompany == 1:
                            isCompany = "Yes"
                        else:
                            isCompany = "No"
                        # Appends the data from the database to the empty list
                        returnData.append({
                            "entityID": entity[0],
                            "name": entity[1],
                            "description": entity[2],
                            "profilePicture": entity[3],
                            "profileBanner": entity[4],
                            "isCompany": isCompany,
                            "isApproved": entity[6]
                        })
                # Returns the array as a JSON
                return json.dumps(returnData)
        # Return a error message if user is not a moderator
        return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401

@community.route('/api/community/listNotApproved/selected/decision', methods=['PUT'])
def get_not_approved_community_Review_descition():
    # Ensures the user is logged in
    if 'UserID' in session:

        # Gets the JSON payload from the request and inherits classes
        data = request.get_json()
        CurrentEntity = data["entityID"]
        decision = data["decision"]

        accountRepository = AccountRepository()
        sitePermissionsRepository = SitePermissionsRepository()
        entitiesRepository = EntitiesRepository()
        entitiesMembersRepository = EntitiesMembersRepository()
        email = Email()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        if perms is not None:
            if perms[1] == 1:
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
