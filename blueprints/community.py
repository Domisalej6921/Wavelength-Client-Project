from flask import Blueprint, render_template, request, redirect, session
from data.ComunityRequestRepository import ComunityRequestRepository

community = Blueprint("community", __name__)
community_repo = ComunityRequestRepository()

@community.route('/create_community')
def create_community():
    return render_template('create_community.html')

# To help me write the following code, I read through one of my team members backend code for creating a POST API route
# The name of the file I learnt from is Registry.py within blueprints
@community.route('/create_community', methods=['POST'])
def create_community_form():
    try:
        data = request.get_json()

        #Checks that data recieved from the POST meets all required fields
        required_fields = ['name', 'description', 'profile_picture', 'profile_banner', 'is_company']
        if not all(field in data for field in required_fields):
            return "There are missing fields", 400

         
        name = data.get('Name')
        description = data.get('Description')
        profile_picture = data.get('ProfilePictureID')
        profile_banner = data.get('BackgroundID')
        is_company = data.get('isCompany')

        #Creating the community
        result = community_repo.Create(name, description, profile_picture, profile_banner, is_company)

        # Success message
        return "Community created successfully", 200
    
    # Learning reasource for Exception groups "https://docs.python.org/3/library/exceptions.html"
    except Exception as e:
        return "Error creating community: " + str(e), 500

if __name__ == '__main__':
    app.run(debug=True)