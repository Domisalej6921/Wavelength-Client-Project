from flask import Flask, Blueprint, render_template, request, redirect, session
import json
import os

# Read appsettings.json and map it onto environ variables
try:
    file = open("appsettings.json", "r")
    settings = json.loads(file.read())
    file.close()

    for key in settings:
        os.environ[key] = str(settings[key])
except:
    raise Exception("Unable to read appsettings.json -> does it exist?")

# Load the Flask app
app = Flask(__name__)

app.secret_key = os.environ['FlaskSecretKey']

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
