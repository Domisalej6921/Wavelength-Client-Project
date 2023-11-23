from data.DataHelper import DataHelper

class VerificationCodesRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def Insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.Execute(
            """INSERT INTO VerificationCodes (UserID, Code, isPasswordCode, Created) VALUES 
            (?, ?, ?, ?)""",
            (data["UserID"], data["Code"], data["isPasswordCode"], data["Created"])
        )