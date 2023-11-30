from flask import Flask, Blueprint, render_template, request, redirect, session , jsonify
import datetime
import os

from logic.cryptography import Cryptography

creditGeneration = Blueprint("creditGeneration", __name__)

@creditGeneration.route("/search", methods=["POST"])
def search():
    search_term = request.json.get("searchTerm")

    response = search_term
    return jsonify(response)

@creditGeneration.route("/create", methods=["POST"])
def create():
    # lets make some fucking credits
    creditsMade = []

    return creditsMade