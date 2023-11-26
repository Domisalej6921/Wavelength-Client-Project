from data.dataHelper import DataHelper

class CommunityRepository():
    def __init__(self):
        self.db = DataHelper()

    def insert(self, data: dict) -> None:
        """Inserts a community into the database."""
        self.db.execute(
            """INSERT INTO Entities (Name, Description, ProfilePictureID, BackgroundID, isCompany, isApproved, Created) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (data["Name"], data["Description"], data["ProfilePictureID"], data["BackgroundID"], data["isCompany"], data["isApproved"], data["Created"])
        )