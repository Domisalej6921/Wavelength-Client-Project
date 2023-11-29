from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import os

from models.footerModel import FooterModel
from models.headerModel import HeaderModel
from data.accountRepository import AccountRepository
from logic.uploads import Uploads

profile = Blueprint('profile', __name__)

@profile.route('/account/profile')
def profilePage():
    if "UserID" in session:
        return render_template("profile.html", footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))
    else:
        return redirect("/login")

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
        if "username" not in data or "profilePicture" not in data or "profileBanner" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check the types of the fields, if they exist
        for item in [('username', str), ('profilePicture', str), ('profileBanner', str)]:
            if item[0] in data:
                if type(data[item[0]]) != item[1]:
                    return "The JSON payload has invalid types!", 400

        # Get the account data from the database and map it to the dictionary for updating
        account = accountRepository.getWithID(userID)
        accountData = {
            "UserID": userID,
            "Username": account[2],
            "ProfilePicture": account[8],
            "BackgroundID": account[9]
        }

        # Check if the username is being changed
        if data["username"] is not None or data["username"] != "":
            # Check if the username is already taken
            if accountRepository.getWithUsername(data["username"]) is not None:
                return "The username is already taken!", 406
            # Otherwise override the username in the dictionary
            accountData["Username"] = data["username"]

        # Check if the profile picture is being changed
        # imageFields = list of tuples: (JSON payload field name, database field name, max size in MB)
        imageFields = [("profilePicture", "ProfilePicture", 2), ("profileBanner", "BackgroundID", 5)]
        for field, dbField, maxSize in imageFields:
            if data[field] is not None or data[field] != "":
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
                uploads.removeImage(imageID)

                uploads.acceptImage(imageID, extension)
                accountData[dbField] = imageID

        # Update the database
        accountRepository.putEditForm(accountData)

        return "Account data has been edited successfully!", 200
    else:
        return "You need to be authenticated to preform this task.", 401
