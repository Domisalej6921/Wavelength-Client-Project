from typing import Union
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

    def getMentorWithLimit(self, limit: int) -> Union[list[tuple], None]:
        """Gets x number of accounts that are mentors"""
        # Used Stackoverflow to help with Orderby
        # Source: https://stackoverflow.com/questions/2051162/sql-multiple-column-ordering
        return self.db.selectWithParams(
            "SELECT * FROM Users WHERE isMentor=1 AND awaitingApproval=0 ORDER BY Created ASC, LastLogin DESC LIMIT ?",
            (limit,))

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

    def getReviewPageData(self):
        return self.db.select(
            """SELECT * FROM Users Where awaitingApproval = 1"""
        )

    def DecisionAccept(self, CurrentAccount: int,):
        """Updates isApproved if the request has been accepted"""
        self.db.execute("UPDATE Users SET awaitingApproval = 0 WHERE UserID = ?", (CurrentAccount, ))

    def DecisionDecline(self, CurrentAccount: int,):
        """Deletes community if the request has been declined"""
        self.db.execute("DELETE FROM Users WHERE UserID = ?", (CurrentAccount, ))
