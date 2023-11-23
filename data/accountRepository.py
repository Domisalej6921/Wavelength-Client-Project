from data.dataHelper import DataHelper

class AccountRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getWithEmail(self, email: str):
        """Gets an account with an email."""
        return self.db.selectFirstWithParams("SELECT * FROM Users WHERE Email = ?", (email,))

    def getWithUsername(self, username: str):
        """Gets an account with a username."""
        return self.db.selectFirstWithParams("SELECT * FROM Users WHERE Username = ?", (username,))

    def insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.execute(
            """INSERT INTO Users (Name, Username, Email, Password, Salt, isMentor, awaitingApproval, Created) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)""",
            (data["name"], data["username"], data["email"], data["password"], data["salt"], data["isMentor"], data["awaitingApproval"], data["created"])
        )