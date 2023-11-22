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

    def Insert(self):
        """Inserts an account into the database."""
        pass