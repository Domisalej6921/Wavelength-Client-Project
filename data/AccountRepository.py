from data.DataHelper import DataHelper

class AccountRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def GetWithEmail(self, email: str):
        """Gets an account with an email."""
        return self.db.SelectFirstWithParams("SELECT * FROM Accounts WHERE Email = ?", (email,))

    def GetWithUsername(self, username: str):
        """Gets an account with a username."""
        return self.db.SelectFirstWithParams("SELECT * FROM Accounts WHERE Username = ?", (username,))

    def Insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.Execute(
            """INSERT INTO Accounts (Name, Username, Email, Password, Salt, isMentor, awaitingApproval, Created) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)""",
            (data["Name"], data["Username"], data["Email"], data["Password"], data["Salt"], data["isMentor"], data["awaitingApproval"], data["Created"])
        )