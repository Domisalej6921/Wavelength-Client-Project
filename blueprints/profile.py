from flask import Flask, Blueprint, render_template, request, redirect, session
from datetime import datetime
import os
import json
from logic.uploads import Uploads
from models.footerModel import FooterModel
from models.headerModel import HeaderModel
from data.accountRepository import AccountRepository
from logic.uploads import Uploads
from data.sitePermissionsRepository import SitePermissionsRepository
from logic.email import Email

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
                if not (type(data[item[0]]) == item[1] or data[item[0]] is None):
                    return "The JSON payload has invalid types!", 400

        # Get the account data from the database and map it to the dictionary for updating
        account = accountRepository.getWithID(userID)
        accountData = {
            "UserID": userID,
            "Username": account[2],
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

                # Otherwise override the profile picture in the dictionary
                # Delete the old image
                uploads.removeImage(accountData[dbField])

                uploads.acceptImage(imageID, extension)
                accountData[dbField] = imageID

        # Update the database
        accountRepository.putEditForm(accountData)

        # Return a success message
        return "Account data has been edited successfully!", 200
    else:
        return "You need to be authenticated to preform this task.", 401


@profile.route('/account/review')
def review_account():
    # Ensures the user is logged in
    if "UserID" in session:
        # Inherits classes
        sitePermissionsRepository = SitePermissionsRepository()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        # Loads the page if the user has the permissions a moderator would have
        if perms is not None:
            if perms[1] == 1:
                return render_template('accountReview.html', footer=FooterModel.standardFooter(), header=HeaderModel.standardHeader())

        # If the user is not a moderator they are sent vack to the account dashboard
        return redirect('/account/dashboard')
    else:
        # If the user is not logged in they are sent to the login page
        return redirect('/login')

@profile.route('/api/account/listNotApproved', methods=['GET'])
def get_not_approved_account():
    # Ensures the user is logged in
    if 'UserID' in session:
        # Inherits classes
        sitePermissionsRepository = SitePermissionsRepository()
        accountRepository = AccountRepository()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        if perms is not None:
            if perms[1] == 1:
                # Retrieving all accounts that are awaiting approval
                accounts = accountRepository.getReviewPageData()
                returnData = []
                if accounts is not None:
                    for account in accounts:
                        # Learnt about the datetime and ctime methods from:
                        # "https://docs.python.org/3/library/datetime.html"
                        dataTimeStamp = account[11]
                        dataDateTime = datetime.fromtimestamp(dataTimeStamp)
                        #Appends the data in the correct format to the empty list
                        returnData.append({
                            "userID": account[0],
                            "name": account[1],
                            "created": dataDateTime.ctime()
                        })
                # Returns the array as a JSON
                return json.dumps(returnData)
        # Return a error message if user is not a moderator
        return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401

@profile.route('/api/account/listNotApproved/selected', methods=['GET'])
def get_not_approved_account_Review():
    # Ensures the user is logged in
    if 'UserID' in session:
        # Learnt how to get parameters from URLs from:
        # "https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask/24892131#24892131"
        CurrentAccount = request.args.get("userID")
        # Inherits classes
        sitePermissionsRepository = SitePermissionsRepository()
        accountRepository = AccountRepository()

        # Gets the Current Users Permissions so further checks can be done to ensure they have permissions
        perms = sitePermissionsRepository.getWithID(int(session['UserID']))

        if perms is not None:
            if perms[1] == 1:
                # Gets data about the current user account from the database
                account = accountRepository.getWithID(int(CurrentAccount))
                returnData = []
                if account is not None:
                    isMentor = account[6]
                    # Returns true and false in a more readable format for the moderator
                    if isMentor == 1:
                        isMentor = "Yes"
                    else:
                        isMentor = "No"
                    # Appends the data from the database to the empty list
                    returnData.append({
                        "userID": account[0],
                        "name": account[1],
                        "userName": account[2],
                        "userEmail": account[3],
                        "isMentor": isMentor,
                        "ProfilePictureID": account[8],
                        "BackgroundID": account[9],
                        "awaitingApproval": account[6]
                    })
                # Returns the array as a JSON
                return json.dumps(returnData)
        # Return a error message if user is not a moderator
        return "You do not have the permissions to execute that command", 403
    else:
        # Return an error message if user is not logged in
        return "You need to be authenticated to preform this task.", 401