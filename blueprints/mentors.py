from flask import *

from data.filesRepository import FilesRepository
from data.accountRepository import AccountRepository

mentors = Blueprint('mentors', __name__)

@mentors.route('/account/dashboard')
def mainPage():
    return render_template('mainPage.html')

@mentors.route('/api/mentors', methods=['POST'])
def mentorSearch():
    if "UserID" in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        filesRepository = FilesRepository()
        accountRepository = AccountRepository()

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
            mentorData = {
                "UserID": mentor[0],
                "Name": mentor[1],
                "Username": mentor[2],
                "ProfilePicture": {},
                "Background": {}
            }
            returnData.append(mentorData)



        return str(data), 200
    else:
        return "You need to be authenticated to preform this task.", 401