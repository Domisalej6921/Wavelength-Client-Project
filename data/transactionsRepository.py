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

    def getAllTransactions(self, tokenId:int):
        """Returns all the data for one token transactions in the current transaction table!"""
        print(self.db.selectWithParams("SELECT * FROM Transactions WHERE TokenID = ?", (tokenId,)))

        return self.db.selectWithParams("SELECT * FROM Transactions WHERE TokenID = ?", (tokenId,))
