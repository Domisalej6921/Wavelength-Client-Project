from data.dataHelper import DataHelper

class TokensRepository:

    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def createTokens(self, newTokenId: int, ownerID: int, ownerType: int, timeCreated: int):
        """Generates the token entries"""

        return self.db.execute(
            "INSERT INTO Tokens (TokenID, OwnerID, isEntity, Created) VALUES (?, ?, ?, ?)",
            (newTokenId, ownerID, ownerType, timeCreated)
        )

    def deleteTokens(self, tokenId: int):
        """Deletes Tokens from the table"""

        return self.db.execute(
            "DELETE FROM Tokens WHERE TokenId = ?",
            (tokenId,)
        )


    def getInactiveTokens(self, date: int):
        """Returns all the inactive tokens IDs and last date used"""

        return self.db.selectWithParams(
            """SELECT Tokens.TokenID, Transactions.Created FROM Tokens
            INNER JOIN Transactions on Tokens.TokenID = Transactions.TokenID
            WHERE Transactions.Created < ? """,
            (date,)
        )

    def getWithUserID(self, UserId: int):
        """Gets Tokens associated with the current user"""
        return self.db.selectWithParams(
            """SELECT * FROM Tokens WHERE Tokens.OwnerID = ? AND Tokens.isEntity = 0""",
            (UserId,)
        )

    def updateOwnerID(self, newOwner: int, tokenId: str):
        """Updating OwnerID following transactions"""
        return self.db.execute(
            """UPDATE Tokens SET OwnerID = ?, isEntity = 1 WHERE TokenID = ?""", (newOwner, tokenId)
        )

