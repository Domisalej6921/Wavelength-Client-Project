from flask import Flask, Blueprint, render_template, request, redirect, session , jsonify
import datetime
import os

from logic.cryptography import Cryptography

creditGeneration = Blueprint("creditGeneration", __name__)

@creditGeneration.route("/listCommunities", methods=["POST"])
def listCommunities():
    communities = []

    return jsonify(communities)

@creditGeneration.route("/search", methods=["POST"])
def search():
    search_term = request.json.get("searchTerm")

    response = search_term
    return jsonify(response)

# CREATE TABLE Entities (
#     EntityID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Name text,
#     Description text,
#     ProfilePictureID integer REFERENCES Files(FileID),
#     BackgroundID integer REFERENCES Files(FileID),
#     isCompany integer,
#     isApproved integer,
#     Created integer
# );

@creditGeneration.route("/create", methods=["POST"])
def create():
    creditsMade = []

    returnedValues = "temporary text"

    creditsMade.append(returnedValues)
    return jsonify(creditsMade)

# CREATE TABLE Tokens (
#     TokenID text NOT NULL PRIMARY KEY,
#     OwnerID integer REFERENCES Entities(EntityID),
#     OwnerType integer,
#     Created integer
# );