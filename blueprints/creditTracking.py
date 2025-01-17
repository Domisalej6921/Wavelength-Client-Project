from flask import Flask, Blueprint, render_template, request, jsonify

from data.transactionsRepository import TransactionsRepository
from data.tokensRepository import TokensRepository
from data.entitiesRepository import EntitiesRepository
from data.accountRepository import AccountRepository

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

@creditTracking.route("/getReceiverName", methods=["POST"])
def getReceiverName():

    receiverId = request.json.get("receiverId")
    isEntity = request.json.get("isEntity")

    if isEntity == 1:
        entitiesRepository = EntitiesRepository()
        entityName = entitiesRepository.getCommunityReturnName(receiverId)

        return jsonify(entityName)

    else:
        accountRepository = AccountRepository()
        usersUsername = accountRepository.getUsernameViaID(receiverId)

        return jsonify(usersUsername)


@creditTracking.route("/getSenderName", methods=["POST"])
def getSenderName():

    senderId = request.json.get("senderId")
    isEntity = request.json.get("isEntity")

    if isEntity == 1:
        entitiesRepository = EntitiesRepository()
        entityName = entitiesRepository.getCommunityReturnName(senderId)

        return jsonify(entityName)

    else:
        accountRepository = AccountRepository()
        usersUsername = accountRepository.getUsernameViaID(senderId)

        return jsonify(usersUsername)

@creditTracking.route("/getChosenCreditTransactions", methods=["POST"])
def getChosenCreditTransactions():

    tokenId = request.json
    transactionsRepository = TransactionsRepository()
    transactions = transactionsRepository.getAllTransactions(tokenId)
    returndata = []

    for transaction in transactions:
        returndata.append(transaction)

    return jsonify(returndata)
