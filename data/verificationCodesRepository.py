from data.dataHelper import DataHelper

class VerificationCodesRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.Execute(
            """INSERT INTO VerificationCodes (UserID, Code, isPasswordCode, Created) VALUES 
            (?, ?, ?, ?)""",
            (data["UserID"], data["Code"], data["isPasswordCode"], data["Created"])
        )