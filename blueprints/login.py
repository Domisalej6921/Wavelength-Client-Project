from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import os

from data.accountRepository import AccountRepository
from data.verificationCodesRepository import VerificationCodesRepository
from logic.cryptography import Cryptography
from logic.email import Email

login = Blueprint('login', __name__)

@login.route('/login')
def loginPage():
    if not ("UserID" in session):
        return render_template('auth/login.html')
    else:
        return redirect("/account/dashboard")

@login.route('/password-reset')
def passwordResetPage():
    if not ("UserID" in session):
        return render_template('auth/passwordReset.html')
    else:
        return redirect("/account/dashboard")

@login.route('/logout')
def logoutAuth():
    if "UserID" in session:
        session.pop("UserID")
        return redirect("/")
    else:
        return redirect("/")

@login.route('/auth/login', methods=['POST'])
def loginAuth():
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

@login.route('/auth/passwordreset-initiate', methods=['POST'])
def passwordResetInitiateAuth():
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
        if "email" not in data:
            return "The JSON payload is missing required fields.", 400

        # Check if the JSON has the correct field types
        if type(data["email"]) is not str:
            return "The JSON payload has incorrect field types.", 400

        # Check if the account exists
        account = accountRepository.getWithEmail(data["email"])
        if account is None:
            return "Account does not exist on our records.", 406

        # All checks have passed so proceed with sending the password reset code

        # Generate a password reset code
        verificationCode = cryptography.createUUID()

        # Sourced from: https://www.tutorialspoint.com/how-to-convert-datetime-to-an-integer-in-python
        currentTime = int(datetime.datetime.now().timestamp())

        # Insert the password reset code into the database
        verificationCodesRepository.insert({
            "userID": account[0],
            "code": verificationCode,
            "isPasswordCode": 1,
            "created": currentTime
        })

        # Send the password reset code to the user via email
        Email.send(
            "Reset your password",
            f"Please follow the link below to reset your account's password\n{os.environ['domain']}/password-reset?code={verificationCode}",
            data["email"])

        # Return a success message
        return "Successfully sent password reset code to email!", 200
    else:
        return "You are already logged into an account.", 400

@login.route('/auth/passwordreset', methods=['PUT'])
def passwordResetAuth():
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
        if "code" not in data or "password" not in data or "repeatPassword" not in data:
            return "The JSON payload is missing required fields.", 400

        # Check if the JSON has the correct field types
        if type(data["code"]) is not str or type(data["password"]) is not str or \
            type(data["repeatPassword"]) is not str:
            return "The JSON payload has incorrect field types.", 400

        # Check if the password is at least 8 characters long
        if len(data["password"]) < 8:
            return "Password must be at least 8 characters long.", 406

        # Check if the passwords match
        if data["password"] != data["repeatPassword"]:
            return "Passwords do not match.", 406

        # Check if the code is valid
        code = verificationCodesRepository.getResetWithCode(data["code"])
        # Check if the code exists
        if code is None:
            return "The code provided is not valid.", 401

        # Sourced from: https://www.tutorialspoint.com/how-to-convert-datetime-to-an-integer-in-python
        currentTime = int(datetime.datetime.now().timestamp())

        # Delete the code from the database
        verificationCodesRepository.delete(code[1])

        # Check if the code has expired
        if currentTime - code[3] >= int(os.environ.get("verificationCodeLifetime")):
            return "The code provided has expired.", 401

        # All checks have passed so proceed with resetting the password

        # Create a salt and hash the password
        salt = cryptography.createSalt()
        hashedPassword = cryptography.digest(data["password"] + salt)

        # Update the password in the database
        accountRepository.putNewPassword({
            "userID": code[0],
            "password": hashedPassword,
            "salt": salt
        })

        # Return a success message
        return "Successfully reset password!", 200
    else:
        return "You are already logged into an account.", 400