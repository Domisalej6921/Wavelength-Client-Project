from data.dataHelper import DataHelper

class VerificationCodesRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getWithVerifyCode(self, code: str):
        """Gets a verification code with a code."""
        return self.db.selectFirstWithParams("SELECT * FROM VerificationCodes WHERE isPasswordCode = ? AND Code = ?", (0, code))

    def insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.execute(
            """INSERT INTO VerificationCodes (UserID, Code, isPasswordCode, Created) VALUES 
            (?, ?, ?, ?)""",
            (data["userID"], data["code"], data["isPasswordCode"], data["created"])
        )

    def delete(self, code: str):
        """Deletes a verification code from the database."""
        self.db.execute("DELETE FROM VerificationCodes WHERE Code = ?", (code,))