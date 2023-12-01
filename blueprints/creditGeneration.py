from flask import Flask, Blueprint, render_template, request, redirect, session , jsonify
import datetime
import os

from logic.cryptography import Cryptography

creditGeneration = Blueprint("creditGeneration", __name__)

def generateTokenId()
    return
def getCommunity(self, name: str, responseId: bool):

    if responseId == True:
        community_Id = "SELECT EntityId FROM Entities WHERE Name IS name"
        return community_Id

    elif responseId == False:
        community_name = "SELECT Name FROM Entities WHERE Name IS name"
        return community_name

def getCommunitiesSimilar(self, searchTerm: str):
    possibleCommunities = []
    possibleCommunities.append("SELECT * FROM Entities WHERE Name LIKE searchTerm")
    return possibleCommunities

def createTokens(self, newTokenId: int, ownerID: int, ownerType: int, timeCreated: int):

    ("INSERT INTO Tokens (TokenID, OwnerID, OwnerType, Created)"
     "VALUES ('newTokenId', 'ownerID', 'ownerType', 'timeCreated')")

    tokenId = newTokenId
    return tokenId

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
def create(data: object):
    creditsMade = []

    tokenIds = []

    while numTokens > 0:
        newTokenId = generateTokenId()
        tokenIds.append(newTokenId)
        communityId = getCommunity(chosenCommunity)
        tokenIds.append(createTokens(newTokenId, communityId))
        numTokens = - 1


    # get the community id
    # generate the token id s
    # assign the token id with the community id and the ownerType(community) add created time

    returnedValues = "temporary text"

    creditsMade.append(returnedValues)
    return jsonify(creditsMade)

# CREATE TABLE Tokens (
#     TokenID text NOT NULL PRIMARY KEY,
#     OwnerID integer REFERENCES Entities(EntityID),
#     OwnerType integer,
#     Created integer
# );