from flask import Flask, Blueprint, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'isodhfudyf8d9asye*sufhsd789fhds89ufhysuifdhsgf78fhasoidhsaidlgho;dhsagofudgfdiosufga9s8dfg7f8s'

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

#Route for main page
from blueprints.main_page import main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
