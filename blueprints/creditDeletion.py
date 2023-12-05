from flask import Flask, Blueprint, render_template, request, jsonify
import datetime

from data.entitiesRepository import EntitiesRepository
from data.tokensRepository import TokensRepository

creditDeletion = Blueprint("creditDeletion", __name__)

def getTime(self):
    return int(datetime.datetime.now().timestamp())

@creditDeletion.route("/getInactiveCredits", methods=["POST"])
def getInacactiveCredits():

    tokensRepository = TokensRepository()
    inactiveCredits = tokensRepository.getInactiveTokens(getTime())

    return jsonify(inactiveCredits)

@creditDeletion.route("/getSelectedInactiveCredits", methods=["POST"])
def getSelectedInactiveCredits():

    return jsonify(selectedCredits)

@creditDeletion.route("/deleteInactiveCredits", methods=["POST"])
def deleteInacactiveCredits():

    for token in tokensToDelete:
        tokensRepository = TokensRepository()
        tokensRepository.deleteTokens(token)