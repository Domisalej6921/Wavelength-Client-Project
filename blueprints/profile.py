from flask import Flask, Blueprint, render_template, request, redirect, session
import datetime
import os

profile = Blueprint('profile', __name__)

@profile.route('/account/profile')
def profilePage():
    if "UserID" in session:
        pass
    else:
        return redirect("/login")