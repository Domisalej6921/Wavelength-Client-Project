from flask import Flask, render_template
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

app.secret_key = os.environ['FlaskSecretKey']


# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Import register blueprint
from blueprints.Register import register
app.register_blueprint(register)

if __name__ == '__main__':
    app.run(debug=True)
