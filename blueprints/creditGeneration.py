from flask import Flask, Blueprint, render_template, request, jsonify
import datetime

from data.entitiesRepository import EntitiesRepository
from data.tokensRepository import TokensRepository
from logic.cryptography import Cryptography

creditGeneration = Blueprint("creditGeneration", __name__)

@creditGeneration.route("/credit-generation")
def creditGenerationPage():
    return render_template("credits/credit-generation.html")

def getTime():
    return int(datetime.datetime.now().timestamp())

def generateTokenId():
    cryptography = Cryptography()
    newTokenId = cryptography.createUUID()
    return newTokenId

@creditGeneration.route("/listCommunities", methods=["GET"])
def listCommunities():

    entitiesRepository = EntitiesRepository()
    communities = entitiesRepository.getCommunitiesOrdered(10)

    returndata = []

    for community in communities:
        returndata.append(community)

    return jsonify(returndata)

@creditGeneration.route("/search", methods=["POST"])
def search():
    search_term = request.json.get("searchTerm")
    if search_term is not None:
        entitiesRepository = EntitiesRepository()
        response = entitiesRepository.getCommunitiesSimilar(search_term)

        if response is not None:
            return jsonify(response)

        return "No matching communities found", 404

    return "Missing 'searchTerm' in the request", 400

@creditGeneration.route("/create", methods=["POST"])
def create():

    data = request.get_json()
    tokenIds = []
    numTokens = data["totalNumCredits"]

    while numTokens > 0:

        newTokenId = generateTokenId()
        tokenIds.append(newTokenId)

        entitiesRepository = EntitiesRepository()
        communityId = entitiesRepository.getCommunityReturnId(data["chosenCommunity"])[0]

        tokensRepository = TokensRepository()
        tokensRepository.createTokens(newTokenId, communityId, 1, getTime())

        numTokens -= 1

    return jsonify(tokenIds)
