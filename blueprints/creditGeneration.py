from flask import Flask, Blueprint, render_template, request, redirect, session , jsonify
import datetime
import os

from data.entitiesRepository import EntitiesRepository
from data.tokensRepository import TokensRepository
from logic.cryptography import Cryptography

creditGeneration = Blueprint("creditGeneration", __name__)

def getTime(self):
    return int(datetime.datetime.now().timestamp())
def generateTokenId(self):
    cryptography = Cryptography()
    newTokenId = cryptography.createUUID()
    return newTokenId

def getCommunitiesSimilar(self, searchTerm: str):
    possibleCommunities = []
    possibleCommunities.append("SELECT * FROM Entities WHERE Name LIKE searchTerm")
    return possibleCommunities

@creditGeneration.route("/listCommunities", methods=["POST"])
def listCommunities():

    entitiesRepository = EntitiesRepository()
    communities = entitiesRepository.getCommunitiesOrdered(10)

    return jsonify(communities)

@creditGeneration.route("/search", methods=["POST"])
def search():
    search_term = request.json.get("searchTerm")
    entitiesRepository = EntitiesRepository()
    response = entitiesRepository.getCommunitiesSimilar(search_term)
    return jsonify(response)

@creditGeneration.route("/create", methods=["POST"])
def create(data: object):
    tokenIds = []
    numTokens = data["totalNumCredits"]

    while numTokens > 0:

        newTokenId = generateTokenId()
        tokenIds.append(newTokenId)

        entitiesRepository = EntitiesRepository()
        communityId = entitiesRepository.getCommunity(data["chosenCommunity"])[1]


        tokensRepository = TokensRepository()
        tokensRepository.createTokens(newTokenId, communityId, 1, getTime())

        numTokens = - 1

    return jsonify(tokenIds)
