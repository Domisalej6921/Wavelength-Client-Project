from flask import Blueprint, render_template, request, redirect, session

community = Blueprint("community", __name__)

@community.route('/create_community')
def create_community():
    return render_template('create_community.html')

#@community.route('')