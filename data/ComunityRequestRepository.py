from data.DataHelper import DataHelper

class ComunityRequestRepository():
    def __init__(self):
        self.db = DataHelper()

    def Create(self, name, description, profilePicture, profileBanner, isCompany):
        # Assuming you have a table named 'Entities'
        query = "INSERT INTO Entities (name, description, profile_picture, profile_banner, is_company) VALUES (?, ?, ?, ?, ?)"
        params = (name, description, profilePicture, profileBanner, isCompany)

        try:
            self.db.Execute(query, params)
            return "Entity created successfully"
        except Exception as e:
            return "Error creating entity: " + str(e)
