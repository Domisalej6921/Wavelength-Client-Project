from data.dataHelper import DataHelper

class AccountRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getWithID(self, userID: int):
        """Gets an account with the user's ID."""
        return self.db.selectFirstWithParams("SELECT * FROM Users WHERE UserID = ?", (userID,))

    def getWithEmail(self, email: str):
        """Gets an account with an email."""
        return self.db.selectFirstWithParams("SELECT * FROM Users WHERE Email = ?", (email,))

    def getWithUsername(self, username: str):
        """Gets an account with a username."""
        return self.db.selectFirstWithParams("SELECT * FROM Users WHERE Username = ?", (username,))

    def putEditForm(self, data: dict):
        """Updates a user's username, profile picture and background."""
        self.db.execute(
            "UPDATE Users SET Username = ?, ProfilePictureID = ?, BackgroundID = ? WHERE UserID = ?",
            (data["Username"], data["ProfilePictureID"], data["BackgroundID"], data["UserID"])
        )

    def putNewPassword(self, data: dict):
        """Updates a user's password."""
        self.db.execute(
            "UPDATE Users SET Password = ?, Salt = ? WHERE UserID = ?",
            (data["password"], data["salt"], data["userID"])
        )

    def insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.execute(
            """INSERT INTO Users (Name, Username, Email, Password, Salt, isMentor, awaitingApproval, Created) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)""",
            (data["name"], data["username"], data["email"], data["password"], data["salt"], data["isMentor"], data["awaitingApproval"], data["created"])
        )
