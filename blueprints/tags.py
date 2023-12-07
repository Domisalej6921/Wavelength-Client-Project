from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import json

from data.tagsRepository import TagsRepository

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
        if type(data["search"]) is not str or type(data["colour"]) is not str:
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