from data.dataHelper import DataHelper

class EntitiesMembersRepository():
    def __init__(self):
        self.db = DataHelper()

    def insert(self, data: dict) -> None:
        """Inserts a community into the database."""
        self.db.execute(
            """INSERT INTO EntityMembers (EntityID, UserID, Role, isAdmin, Created) 
            VALUES (?, ?, ?, ?, ?)""",
            (data["EntityID"], data["UserID"], data["Role"], data["isAdmin"], data["Created"])
        )

    def GetWithEntity(self, entityId):
        """Gets data with EntityID"""
        return self.db.selectFirstWithParams("SELECT UserID FROM EntityMembers WHERE EntityID= ?", (entityId,))
