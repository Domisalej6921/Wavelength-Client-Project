from flask import *

from data.filesRepository import FilesRepository
from data.accountRepository import AccountRepository
from data.assignedTagsRepository import AssignedTagsRepository
from models.footerModel import FooterModel
from models.headerModel import HeaderModel

mentors = Blueprint('mentors', __name__)

@mentors.route('/account/dashboard')
def mainPage():
    return render_template('mainPage.html', footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))

@mentors.route('/account/mentor_apply')
def mentor_apply():
    return render_template('mentorApp.html', footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))

@mentors.route('/account/become_mentor')
def become_mentor():
    return render_template('becomeMentor.html', footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))

@mentors.route('/api/mentors', methods=['POST'])
def mentorSearch():
    if "UserID" in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        filesRepository = FilesRepository()
        accountRepository = AccountRepository()
        assignedTagsRepository = AssignedTagsRepository()

        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if there is at least one valid field in the JSON payload
        if "limit" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["limit"]) is not int:
            return "The JSON payload has incorrect field types!", 400

        if data["limit"] > 100:
            data["limit"] = 100

        returnData = []

        mentors = accountRepository.getMentorWithLimit(data["limit"])

        for mentor in mentors:
            # Define the JSON for each mentor
            mentorData = {
                "userID": mentor[0],
                "name": mentor[1],
                "username": mentor[2],
                "description": mentor[6],
                "tags": [],
                "profilePicture": {
                    "path": "",
                    "alt": ""
                },
                "background": {
                    "path": "",
                    "alt": ""
                }
            }

            # Get the images using a list of tuples
            images = [('profilePicture', mentor[9]), ('background', mentor[10])]
            for path, imageID in images:
                try:
                    # Get the image data from the Files table
                    imageData = filesRepository.getWithID(imageID)

                    # Update the mentorData directory
                    mentorData[path]['path'] = f'{imageData[1]}.{imageData[2]}'
                    mentorData[path]['alt'] = imageData[3]
                except:
                    mentorData[path]['path'] = ''
                    mentorData[path]['alt'] = ''

            tags = assignedTagsRepository.getWithUserID(mentor[0])
            for tag in tags:
                mentorData["tags"].append({
                    "tagID": tag[0],
                    "name": tag[1],
                    "colour": tag[2]
                })

            returnData.append(mentorData)

        # Used W3schools to help convert json to string
        # Source: https://www.w3schools.com/python/python_json.asp
        return json.dumps(returnData), 200
    else:
        return "You need to be authenticated to preform this task.", 401