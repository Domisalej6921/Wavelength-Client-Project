from flask import Flask, Blueprint, render_template, request, jsonify
import datetime

from data.entitiesRepository import EntitiesRepository
from data.tokensRepository import TokensRepository

creditDeletion = Blueprint("creditDeletion", __name__)

@creditDeletion.route("/credit-deletion")
def creditDeletionPage():
    return render_template("credits/delete-credits.html")

def getTime():
    return int(datetime.datetime.now().timestamp())

@creditDeletion.route("/getInactiveCredits", methods=["POST"])
def getInacactiveCredits():

    tokensRepository = TokensRepository()
    inactiveCredits = tokensRepository.getInactiveTokens((getTime()-2592000))
    print(inactiveCredits)

    return jsonify(inactiveCredits)

@creditDeletion.route("/getChosenInactiveCredits", methods=["POST"])
def getSelectedInactiveCredits():

    timeInactive = request.json.get("creditAgeValue")
    if timeInactive is not None:

        tokensRepository = TokensRepository()
        selectedCredits = tokensRepository.getInactiveTokens((getTime() - timeInactive))
        print(selectedCredits)

        if selectedCredits is not None:
            return jsonify(selectedCredits)

        return "No matching communities found", 404

    return "Missing 'searchTerm' in the request", 400

@creditDeletion.route("/deleteInactiveCredits", methods=["POST"])
def deleteInacactiveCredits():

    for token in tokensToDelete:
        tokensRepository = TokensRepository()
        tokensRepository.deleteTokens(token)