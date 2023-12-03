from data.dataHelper import DataHelper

class CommunityMembersRepository():
    def __init__(self):
        self.db = DataHelper()

    def insert(self, data: dict) -> None:
        """Inserts a community into the database."""
        self.db.execute(
            """INSERT INTO EntityMembers (EntityID, UserID, Role, isAdmin, Created) 
            VALUES (?, ?, ?, ?, ?)""",
            (data["EntityID"], data["UserID"], data["Role"], data["isAdmin"], data["Created"])
        )