from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import os

from data.accountRepository import AccountRepository
from data.verificationCodesRepository import VerificationCodesRepository
from logic.cryptography import Cryptography
from logic.email import Email

login = Blueprint('login', __name__)

@login.route('/login')
def login_page():
    if not ("UserID" in session):
        return render_template('auth/login.html')
    else:
        return redirect("/account/dashboard")

@login.route('/auth/login', methods=['POST'])
def login_auth():
    if not ("UserID" in session):
        # Get the JSON payload from the request and inherit classes
        data = request.get_json()

        accountRepository = AccountRepository()
        verificationCodesRepository = VerificationCodesRepository()
        cryptography = Cryptography()

        # Run a series of validation checks on the JSON payload

        # Check if the JSON exists
        if data is None:
            return "No JSON payload was uploaded with the request!", 400

        # Check if the JSON has the required fields
        if "email" not in data or "password" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if type(data["email"]) is not str or type(data["password"]) is not str:
            return "The JSON payload has incorrect field types!", 400

        # Check if the account exists
        account = accountRepository.getWithEmail(data["email"])
        if account is None:
            return "Invalid authentication credentials.", 401

        # Check if the passwords match
        if not (cryptography.verifyPassword(data["password"] + account[5], account[4])):
            return "Invalid authentication credentials.", 401

        # Check if the account's email is verified
        code = verificationCodesRepository.getVerifyWithUserID(account[0])
        if code is not None:
            return "Your email address is not verified.", 403

        # All checks have passed so proceed with login
        session["UserID"] = account[0]

        # Return a success message
        return "Successfully logged in!", 200
    else:
        return "You are already logged into an account.", 400