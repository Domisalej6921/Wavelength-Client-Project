from flask import Flask, Blueprint, render_template, request, redirect, session
import json
import os

from models.footerModel import FooterModel
from models.headerModel import HeaderModel
from data.accountRepository import AccountRepository
from data.filesRepository import FilesRepository
from data.tagsRepository import TagsRepository
from logic.uploads import Uploads

profile = Blueprint('profile', __name__)

@profile.route('/account/profile')
def profilePage():
    if "UserID" in session:
        return render_template("profile.html", footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))
    else:
        return redirect("/login")

@profile.route('/api/profile', methods=['POST'])
def profileDetails():
    if 'UserID' in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        accountRepository = AccountRepository()
        filesRepository = FilesRepository()
        tagsRepository = TagsRepository()

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if the JSON has the required fields
        if "userID" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["userID"]) is not int:
            return "The JSON payload has incorrect field types!", 400

        # If the ID is 0 then use the session ID
        if data["userID"] == 0:
            data["userID"] = int(session["UserID"])

        # Get the account data from the database
        account = accountRepository.getWithID(data["userID"])

        # Check if the account exists
        if account is None:
            return "This account does not exist!", 404

        # Check if the account is the same as the one requesting the data
        isMyAccount = False
        if account[0] == int(session["UserID"]):
            isMyAccount = True

        # Create a JSON object to return
        returnData = {
            "userID": account[0],
            "username": account[2],
            "description": account[12],
            "tags": [],
            "isMentor": bool(account[6]),
            "awaitingApproval": bool(account[7]),
            "profilePicture": None,
            "profileBanner": None,
            "isMyAccount": isMyAccount
        }

        # Get the tags from the database, then loop through and format them
        tags = tagsRepository.getWithUserID(account[0])
        for tag in tags:
            returnData["tags"].append({
                "tagID": tag[0],
                "name": tag[1],
                "colour": tag[2]
            })

        # Get the profile picture and profile banner from the database
        imageFields = [("profilePicture", 8), ("profileBanner", 9)]
        for image, i in imageFields:
            picture = filesRepository.getWithID(account[i])

            # Check if the profile picture exists
            if picture is not None:
                returnData[image] = {
                    "path": "/static/uploads/" + picture[1] + "." + picture[2],
                    "description": picture[3]
                }

        # Return the JSON object
        return json.dumps(returnData), 200
    else:
        return "You need to be authenticated to preform this task.", 401

@profile.route('/api/profile-edit', methods=['POST'])
def profileEditApi():
    if "UserID" in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        accountRepository = AccountRepository()
        uploads = Uploads()

        # Get the userID from the session
        userID = int(session["UserID"])

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if there is at least one valid field in the JSON payload
        if "username" not in data or "description" not in data or "profilePicture" not in data or "profileBanner" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check the types of the fields, if they exist
        for item in [('username', str), ('description', str), ('profilePicture', str), ('profileBanner', str)]:
            if item[0] in data:
                if not (type(data[item[0]]) == item[1] or data[item[0]] is None):
                    return "The JSON payload has invalid types!", 400

        # Get the account data from the database and map it to the dictionary for updating
        account = accountRepository.getWithID(userID)
        accountData = {
            "UserID": userID,
            "Username": account[2],
            "Description": account[12],
            "ProfilePictureID": account[8],
            "BackgroundID": account[9]
        }

        # Check if the username is being changed
        if data["username"] is not None:
            # Check if the username is valid
            if len(data["username"]) < 3 or len(data["username"].split(" ")) > 1:
                return "This username is invalid! It must be at least 3 characters and contain no whitespace.", 406
            # Check if the username is already taken
            if accountRepository.getWithUsername(data["username"]) is not None:
                return "The username is already taken!", 406
            # Otherwise override the username in the dictionary
            accountData["Username"] = data["username"]

        # Check if the description is being changed
        if data["description"] is not None:
            # Check if the description is valid
            if len(data["description"]) >= 2000:
                return "The description is too long! It must be less than or equal to 2000 characters.", 406
            # Otherwise override the description in the dictionary
            accountData["Description"] = data["description"]

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
                    return f"The profile picture is too large! Max size is {maxSize}MB", 406
                elif extension not in os.environ["allowedFileExtensions"]:
                    uploads.rejectImage(imageID, extension)
                    return "The profile picture does not use a valid file extension", 406

                # Otherwise override the profile picture in the dictionary
                # Delete the old image
                uploads.removeImage(accountData[dbField])

                uploads.acceptImage(imageID, extension)
                accountData[dbField] = imageID

        # Update the database
        accountRepository.putEditForm(accountData)

        return "Account data has been edited successfully!", 200
    else:
        return "You need to be authenticated to preform this task.", 401
