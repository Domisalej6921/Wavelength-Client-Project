from data.DataHelper import DataHelper

class AccountRepository:
    # Inherit the DataHelper class
    db = DataHelper()

    @staticmethod
    def GetWithEmail(self, email: str):
        """Gets an account with an email."""
        return self.db.SelectFirstWithParams("SELECT * FROM Accounts WHERE Email = ?", (email,))

    @staticmethod
    def GetWithUsername(self, username: str):
        """Gets an account with a username."""
        return self.db.SelectFirstWithParams("SELECT * FROM Accounts WHERE Username = ?", (username,))

    @staticmethod
    def Insert(self):
        """Inserts an account into the database."""
        pass