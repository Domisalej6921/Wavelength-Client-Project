import
from data.dataHelper import DataHelper

class TokensRepository:

    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()


    def createTokens(self, newTokenId: int, ownerID: int, ownerType: int, timeCreated: int):
        """Generates the token entries"""

        return self.db.execute(
            """INSERT INTO Tokens (TokenID, OwnerID, OwnerType, Created) VALUES (?, ?, ?, ?)""",
            (newTokenId, ownerID, ownerType, timeCreated)
        )