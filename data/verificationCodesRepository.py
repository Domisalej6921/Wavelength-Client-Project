from data.dataHelper import DataHelper

class VerificationCodesRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.execute(
            """INSERT INTO VerificationCodes (UserID, Code, isPasswordCode, Created) VALUES 
            (?, ?, ?, ?)""",
            (data["userID"], data["code"], data["isPasswordCode"], data["created"])
        )