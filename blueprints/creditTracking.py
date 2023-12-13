from flask import Flask, Blueprint, render_template, request, jsonify

from data.transactionsRepository import TransactionsRepository
from data.tokensRepository import TokensRepository

creditTracking = Blueprint("creditTracking", __name__)

@creditTracking.route("/credit-tracking")
def creditTrackingPage():
    return render_template("credits/transaction-tracking.html")

@creditTracking.route("/getCredits", methods=["GET"])
def getCredits():

    tokensRepository = TokensRepository()
    credits = tokensRepository.getAllTokens(True)
    returndata = []

    for credit in credits:
        returndata.append(credit)

    return jsonify(returndata)

@creditTracking.route("/getReceiverName", methods=["GET"])
def getReceiverName():

    receiverId = request.json[0]
    isEntity = request.json[1]

    if isEntity == 1:

        return jsonify(entityName)

    else:

        return jsonify(usersName)


@creditTracking.route("/getSenderName", methods=["GET"])
def getSenderName():

    senderId = request.json[0]
    isEntity = request.json[1]

    if isEntity == 1:

        return jsonify(entityName)

    else:

        return jsonify(usersName)

@creditTracking.route("/getChosenCreditTransactions", methods=["POST"])
def getChosenCreditTransactions():

    tokenId = request.json
    transactionsRepository = TransactionsRepository()
    transactions = transactionsRepository.getAllTransactions(tokenId)
    returndata = []

    for transaction in transactions:
        returndata.append(transaction)

    return jsonify(returndata)
