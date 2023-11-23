from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import os

from data.accountRepository import AccountRepository
from data.verificationCodesRepository import VerificationCodesRepository
from logic.cryptography import Cryptography
from logic.email import Email

register = Blueprint('register', __name__)

@register.route('/register')
def register_page():
    if not ("UserID" in session):
        return render_template('auth/register.html')
    else:
        return redirect("/account/dashboard")

@register.route('/verify')
def verify_auth():
    if not ("UserID" in session):
        # Get the code from the URL and inherit classes
        code = request.args.get("code")

        verificationCodesRepository = VerificationCodesRepository()

        # Check if the code exists
        if code is not None:
            data = verificationCodesRepository.getVerifyWithCode(code)
            if data is not None:
                # Delete the verification code and redirect to the login page
                verificationCodesRepository.delete(code)
                return redirect("/login")

        return render_template('auth/verify.html')
    else:
        return redirect("/account/dashboard")

@register.route('/auth/register', methods=['POST'])
def register_auth():
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
        if "name" not in data or "username" not in data or "email" not in data or \
                "password" not in data or "repeatPassword" not in data or "isMentor" not in data:
            return "The JSON payload is missing required fields!", 400

        # Check if the JSON has the correct field types
        if not type(data["name"]) is str or not type(data["username"]) is str or not type(data["email"]) is str or \
                not type(data["password"]) is str or not type(data["repeatPassword"]) is str or not type(data["isMentor"]) is bool:
            return "The JSON payload has incorrect field types!", 400

        # Check if the password is long enough
        if len(data["password"]) < 8:
            return "The password must be at least 8 characters long!", 406

        # Check if the email is valid
        if "@" not in data["email"] or "." not in data["email"]:
            return "This email is invalid! It must contain a '@' symbol and a '.' character", 406

        # Check if the username is valid
        if len(data["username"]) < 3 or len(data["username"].split(" ")) > 1:
            return "This username is invalid! It must be at least 3 characters and contain no whitespace.", 406

        # Check if the email is already in use
        if accountRepository.getWithEmail(data["email"]) is not None:
            return "This email is already in use!", 406

        # Check if the username is already in use
        if accountRepository.getWithUsername(data["username"]) is not None:
            return "This username is already in use!", 406

        # All checks have passed so proceed with registration

        # Create a salt and hash the password
        salt = cryptography.createSalt()
        hashedPassword = cryptography.digest(data["password"] + salt)

        # Sourced from: https://www.tutorialspoint.com/how-to-convert-datetime-to-an-integer-in-python
        currentTime = int(datetime.datetime.now().timestamp())

        # Insert the account into the database
        # Check if the user is a mentor and if so set awaitingApproval to true
        if data["isMentor"]:
            accountRepository.insert({
                "name": data["name"],
                "username": data["username"],
                "email": data["email"],
                "password": hashedPassword,
                "salt": salt,
                "isMentor": data["isMentor"],
                "awaitingApproval": True,
                "created": currentTime
            })
        else:
            accountRepository.insert({
                "name": data["name"],
                "username": data["username"],
                "email": data["email"],
                "password": hashedPassword,
                "salt": salt,
                "isMentor": data["isMentor"],
                "awaitingApproval": False,
                "created": currentTime
            })

        # Create a verification code
        verificationCode = cryptography.createUUID()

        # Send the verification code to the user via email
        Email.send(
            "Verify your email address",
            f"Please follow the link below to verify your account\n{os.environ['domain']}/verify?code={verificationCode}",
            data["email"])

        # Insert the verification code into the database
        verificationCodesRepository.insert({
            "userID": accountRepository.getWithEmail(data["email"])[0],
            "code": verificationCode,
            "isPasswordCode": False,
            "created": currentTime
        })

        # Return a success message
        return "Account created successfully!", 200
    else:
        return "You are already logged into an account.", 400
