from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import os

from data.accountRepository import AccountRepository
from data.verificationCodesRepository import VerificationCodesRepository
from logic.cryptography import Cryptography
from logic.email import Email

register = Blueprint('login', __name__)

@register.route('/login')
def login_page():
    if not ("UserID" in session):
        return render_template('auth/login.html')
    else:
        return redirect("/account/dashboard")
