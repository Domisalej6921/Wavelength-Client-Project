from flask import Blueprint, render_template, request, redirect, session
from datetime import datetime

from data.communityRepository import CommunityRepository
from data.accountRepository import AccountRepository

community = Blueprint("community", __name__)

@community.route('/community/create')
def create_community():
    return render_template('createCommunity.html')

# To help me write the following code, I read through one of my team members backend code for creating a POST API route
# The name of the file I learnt from is Registry.py within blueprints
@community.route('/api/community/create', methods=['POST'])
def create_community_form():
    if "UserID" in session:
        # Gets the JSON payload from the request and inherits classes
        data = request.get_json()

        communityRepository = CommunityRepository()
        accountRepository = AccountRepository()

        # Get the userID from the session cookie
        userID = int(session["UserID"])

        # Learnt about HTTP status codes from "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes"
        # The status codes return to the JS file to help the client understand the nature of the issue

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Checks that data recieved from the POST meets all required fields
        if data not in ['name', 'description', 'isCompany']:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["name"]) is not str or type(data["description"]) is not str or type(data["isCompany"]) is not bool:
            return "The JSON payload has incorrect field types!", 400
        
        # Get the user's account and check if the user if they have permissions to create a community
        account = accountRepository.getWithID(userID)
        if account[6] == 0:
            return "Your account does not have permissions for this action.", 403

        # Assigns the variable to the set file extentions in the app settings JSON file
        allowedFileExtensions = os.environ["allowedFileExtensions"]

        # Gets the profile picture, and ensures it is the correct file type and then checks if its under 2MB
        fileName, extension, size = checkImage(data["ProfilePictureID"])
        if extention not in allowedFileExtensions:
            return "The JSON payload has incorrect profile picure type!", 406
        if size > 2:
            return "The Profile picure size is to large, needs to be less than 2MB", 406
        # Gets the profile banner, and ensures it is the correct file type and then checks if its under 5MB
        fileName, extension, size = checkImage(data["BackgroundID"])
        if extention not in allowedFileExtensions:
            return "The JSON payload has incorrect profile banner type!", 406
        if size > 5:
            return "The Profile banner size is to large, needs to be less than 5MB", 406

        communityRepository.insert({
            "Name": data["name"],
            "Description": data["description"],
            "ProfilePictureID": data["profilePicture"],
            "BackgroundID": data["profileBanner"],
            "isCompany": int(data["isCompany"]),
            "isApproved": 0,
            "Created": int(datetime.datetime.now().timestamp())
        })

        # Success message
        return "Community created successfully", 200
    else:
        return "You need to be authenticated to preform this task.", 401

if __name__ == '__main__':
    app.run(debug=True)