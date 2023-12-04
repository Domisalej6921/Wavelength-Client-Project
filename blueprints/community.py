from flask import Blueprint, render_template, request, redirect, session
from datetime import datetime
import os
from data.communityRepository import CommunityRepository
from data.communityMembersRepository import CommunityMembersRepository
from data.accountRepository import AccountRepository
from logic.uploads import Uploads
from models.footerModel import FooterModel
from models.headerModel import HeaderModel

community = Blueprint("community", __name__)


@community.route('/community/create')
def create_community():
    return render_template('createCommunity.html', footer=FooterModel.standardFooter(), header=HeaderModel.standardHeader())


# To help me write the following code, I read through one of my team members backend code for creating a POST API route
# The name of the file I learnt from is Registry.py within blueprints
@community.route('/api/community/create', methods=['POST'])
def create_community_form():
    if "UserID" in session:
        # Gets the JSON payload from the request and inherits classes
        data = request.get_json()

        communityRepository = CommunityRepository()
        communityMembersRepository = CommunityMembersRepository()
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
        if not all(field in data for field in ['name', 'description', 'isCompany']):
            return "The JSON payload is missing required fields!", 400

        # Checks if the JSON has empty fields for name and description
        if data['name'] == "" or data['description'] == "":
            return "The JSON payload contains empty fields!", 400

        # Check if the JSON has the correct field types
        # Learnt about the isdigit method from "https://www.w3schools.com/python/ref_string_isdigit.asp"
        if data['name'].isdigit() or data['description'].isdigit():
            return "The JSON payload has incorrect field types!", 400

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
            "Created": datetime.now().timestamp()
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
        communityRepository.insert(communityData)

        # Get the new community's ID
        communityID = int(communityRepository.getIDWithProfilePictureID(communityData["ProfilePictureID"])[0])

        # Insert the user into the community members table
        communityMembersRepository.insert({
            "EntityID": communityID,
            "UserID": userID,
            "Role": "Founder",
            "isAdmin": 1,
            "Created": datetime.now().timestamp()
        })

        # Return a success message
        return "Community created successfully", 200
    else:
        return "You need to be authenticated to preform this task.", 401
