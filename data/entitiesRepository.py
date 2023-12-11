from data.dataHelper import DataHelper

class EntitiesRepository():
    def __init__(self):
        self.db = DataHelper()

    def getIDWithProfilePictureID(self, profilePictureID: str):
        """Gets a community's ID with a profile picture ID."""
        return self.db.selectFirstWithParams("SELECT EntityID FROM Entities WHERE ProfilePictureID = ?", (profilePictureID,))

    def insert(self, data: dict) -> None:
        """Inserts a community into the database."""
        self.db.execute(
            """INSERT INTO Entities (Name, Description, ProfilePictureID, BackgroundID, isCompany, isApproved, Created) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (data["Name"], data["Description"], data["ProfilePictureID"], data["BackgroundID"], data["isCompany"], data["isApproved"], data["Created"])
        )