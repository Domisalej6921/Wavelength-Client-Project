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

<<<<<<< HEAD
=======
from models.footerModel import FooterModel
from models.headerModel import HeaderModel

>>>>>>> 9dfe5d72ce42109eccb1d6cb0c8b0b9a466a1095
# Route for the index page
@app.route('/')
def index():
    return render_template('index.html', footer=FooterModel.standardFooter(), header=HeaderModel.renderHeader(session))

#Route for main page
from blueprints.mentorsPage import main_blueprint
app.register_blueprint(main_blueprint)

# Import register blueprint
from blueprints.register import register
app.register_blueprint(register)

# Import login blueprint
from blueprints.login import login
app.register_blueprint(login)

# Import profile blueprint
from blueprints.profile import profile
app.register_blueprint(profile)

if __name__ == '__main__':
    app.run(debug=True)
