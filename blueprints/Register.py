from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime

from data.AccountRepository import AccountRepository
from data.VerificationCodesRepository import VerificationCodesRepository
from logic.Cryptography import Cryptography
from logic.Email import Email

register = Blueprint('register', __name__)


@register.route('/register')
def register_page():
    return render_template('auth/register.html')


@register.route('/auth/register', methods=['POST'])
def register_auth():
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
    if "Name" not in data or "Username" not in data or "Email" not in data or \
            "Password" not in data or "isMentor" not in data:
        return "The JSON payload is missing required fields!", 400

    # Check if the JSON has the correct field types
    if not type(data["Name"]) is str or not type(data["Username"]) is str or not type(data["Email"]) is str or \
            not type(data["Password"]) is str or not type(data["isMentor"]) is bool:
        return "The JSON payload has incorrect field types!", 400

    # Check if the password is long enough
    if len(data["Password"]) < 8:
        return "The password must be at least 8 characters long!", 406

    # Check if the email is valid
    if "@" not in data["Email"] or "." not in data["Email"]:
        return "This email is invalid! It must contain a '@' symbol and a '.' character", 406

    # Check if the username is valid
    if len(data["Username"]) < 3 or len(data.split(" ")) > 1:
        return "This username is invalid! It must be at least 3 characters and contain no whitespace.", 406

    # Check if the email is already in use
    if accountRepository.GetWithEmail(data["Email"]) is not None:
        return "This email is already in use!", 406

    # Check if the username is already in use
    if accountRepository.GetWithUsername(data["Username"]) is not None:
        return "This username is already in use!", 406

    # All checks have passed so proceed with registration

    # Create a salt and hash the password
    salt = cryptography.CreateSalt()
    hashedPassword = cryptography.Digest(data["Password"] + salt)

    # Sourced from: https://www.tutorialspoint.com/how-to-convert-datetime-to-an-integer-in-python
    currentTime = int(datetime.datetime.now().timestamp())

    # Insert the account into the database
    # Check if the user is a mentor and if so set awaitingApproval to true
    if data["isMentor"]:
        accountRepository.Insert({
            "Name": data["Name"],
            "Username": data["Username"],
            "Email": data["Email"],
            "Password": hashedPassword,
            "Salt": salt,
            "isMentor": data["isMentor"],
            "awaitingApproval": True,
            "Created": currentTime
        })
    else:
        accountRepository.Insert({
            "Name": data["Name"],
            "Username": data["Username"],
            "Email": data["Email"],
            "Password": hashedPassword,
            "Salt": salt,
            "isMentor": data["isMentor"],
            "awaitingApproval": False,
            "Created": currentTime
        })

    # Create a verification code
    verificationCode = cryptography.CreateUUID()

    # Send the verification code to the user via email
    Email.Send("Verify your email address", f"Your verification code is: {verificationCode}", data["Email"])

    # Insert the verification code into the database
    verificationCodesRepository.Insert({
        "UserID": accountRepository.GetWithEmail(data["Email"])[0],
        "Code": verificationCode,
        "isPasswordCode": False,
        "Created": currentTime
    })

    # Return a success message
    return "Account created successfully!", 200
