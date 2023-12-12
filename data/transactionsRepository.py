from data.dataHelper import DataHelper

class TransactionsRepository:

    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def createTransactionLog(self, tokenId: str, senderId: int, isSenderEntity: bool, receiverId: int, isReceiverEntity: bool, isDonation: bool, timeCreated: int):
        """Generates the transaction for the token"""
        if isSenderEntity:
            isSenderEntity = 1
        else:
            isSenderEntity = 0
        if isReceiverEntity:
            isReceiverEntity = 1
        else:
            isReceiverEntity = 0
        if isDonation:
            isDonation = 1
        else:
            isDonation = 0


        return self.db.execute(
            """INSERT INTO Transactions (TokenID, SenderID, isSenderEntity, ReceiverID, isReceiverEntity, isDonation, Created) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (tokenId, senderId, isSenderEntity, receiverId, isReceiverEntity, isDonation, timeCreated)
        )
