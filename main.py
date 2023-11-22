from flask import Flask, Blueprint, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'isodhfudyf8d9asye*sufhsd789fhds89ufhysuifdhsgf78fhasoidhsaidlgho;dhsagofudgfdiosufga9s8dfg7f8s'

# Route for the index page ----- delete after --- commented index out so that I could view the main page
#@app.route('/')
#def index():
    #return render_template('index.html')

#Route for main page
@app.route('/')
def main_page():
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(debug=True)
