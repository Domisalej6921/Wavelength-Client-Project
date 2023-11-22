from flask import Flask, Blueprint, render_template, request, redirect, session

register = Blueprint('register', __name__)

@register.route('/register')
def register_page():
    return render_template('auth/register.html')

@register.route('/auth/register', methods=['POST'])
def register_auth():
    data = request.json
