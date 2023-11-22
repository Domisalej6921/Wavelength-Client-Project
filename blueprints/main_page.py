from flask import *

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/main_page')
def main_page():
    return render_template('main_page.html')