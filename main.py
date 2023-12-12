from flask import Flask, render_template, session
import json
import os

# Used https://stackoverflow.com/questions/19663093/apply-gitignore-on-an-existing-repository-already-tracking-large-number-of-file
# to help with .gitignore

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

app.secret_key = os.environ['flaskSecretKey']

from models.footerModel import FooterModel
from models.headerModel import HeaderModel

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html', footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))

# Import register blueprint
from blueprints.register import register
app.register_blueprint(register)

# Import login blueprint
from blueprints.login import login
app.register_blueprint(login)

# Import credit generation blueprint
from blueprints.creditGeneration import creditGeneration
app.register_blueprint(creditGeneration)

# Import credit deletion blueprint
from blueprints.creditDeletion import creditDeletion
app.register_blueprint(creditDeletion)

# Add community Blueprint
from blueprints.community import community
app.register_blueprint(community)

# Import profile blueprint
from blueprints.profile import profile
app.register_blueprint(profile)

if __name__ == '__main__':
    app.run(debug=True)
