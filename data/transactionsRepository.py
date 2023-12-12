from data.dataHelper import DataHelper

class TransactionsRepository:

    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def createTransactionLog(self, tokenId: str, senderId: int, receiverId: int, isDonation: bool, timeCreated: int):
        """Generates the transaction for the token"""
        if isDonation:
            isDonation = 1
        else:
            isDonation = 0


        return self.db.execute(
            """INSERT INTO Transactions (TokenID, SenderID, ReceiverID, isDonation, Created) 
            VALUES (?, ?, ?, ?, ?)""",
            (tokenId, senderId, receiverId, isDonation, timeCreated)
        )
