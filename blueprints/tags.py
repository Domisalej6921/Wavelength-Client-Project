from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import json

from data.tagsRepository import TagsRepository
from data.assignedTagsRepository import AssignedTagsRepository

tags = Blueprint('tags', __name__)

@tags.route('/api/tags-search', methods=['POST'])
def tagsSearch():
    if 'UserID' in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        tagsRepository = TagsRepository()

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if the JSON has the required fields
        if "search" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["search"]) is not str:
            return "The JSON payload has incorrect field types!", 400

        # Get the tags from the database
        tags = tagsRepository.getWithSearch(data["search"])

        # Create a JSON object to return
        returnData = []

        # Loop through the tags
        for tag in tags:
            # Create a JSON object for the tag
            if tag[0] is not None:
                tagData = {
                    "tagID": tag[0],
                    "name": tag[1],
                    "colour": tag[2]
                }

                # Add the tag to the return data
                returnData.append(tagData)

        # Return the JSON object
        return json.dumps(returnData), 200
    else:
        return "You need to be authenticated to preform this task.", 401

@tags.route('/api/tags-assign', methods=['PUT'])
def tagsAssign():
    if 'UserID' in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        tagsRepository = TagsRepository()
        assignedTagsRepository = AssignedTagsRepository()

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if the JSON has the required fields
        if "tagID" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["tagID"]) is not int:
            return "The JSON payload has incorrect field types!", 400

        # Check if the tag exists
        tag = tagsRepository.getWithID(data["tagID"])
        if tag is None:
            return "The tag does not exist!", 406

        # Check if the tag is already assigned to the user
        assignedTag = assignedTagsRepository.getWithUserIDAndTagID(session["UserID"], data["tagID"])
        if assignedTag is not None:
            return "The tag is already assigned to the user!", 406

        # Check if the user has more than 10 tags assigned to them
        assignedTags = assignedTagsRepository.getWithUserID(session["UserID"])
        if len(assignedTags) >= 10:
            return "Maximum number of tags assigned to user account.", 406

        # Assign the tag to the user
        assignedTagsRepository.insert({
            "TagID": data["tagID"],
            "UserID": int(session["UserID"]),
            "Created": int(datetime.datetime.now().timestamp())
        })

        # Return a success message
        return "The tag was successfully assigned!", 200
    else:
        return "You need to be authenticated to preform this task.", 401

@tags.route('/api/tags-add', methods=['POST'])
def tagsAdd():
    if 'UserID' in session:
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        tagsRepository = TagsRepository()

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if the JSON has the required fields
        if "name" not in data or "colour" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["name"]) is not str or type(data["colour"]) is not str:
            return "The JSON payload has incorrect field types!", 400

        # Insert the tag into the database
        tagsRepository.insert({
            "CreatedBy": session["UserID"],
            "Name": data["name"],
            "Colour": data["colour"],
            "Created": int(datetime.datetime.now().timestamp())
        })

        # Return a success message
        return "The tag was successfully added!", 200
    else:
        return "You need to be authenticated to preform this task.", 401