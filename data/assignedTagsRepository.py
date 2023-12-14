from typing import Union
from data.dataHelper import DataHelper

class AssignedTagsRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getWithUserID(self, userID: int) -> Union[list[tuple], None]:
        """Gets all assigned tags with a userID."""
        return self.db.selectWithParams(
            """SELECT T.TagID, T.Name, T.Colour
            FROM AssignedTags AS AT
            INNER JOIN Tags AS T ON AT.TagID = T.TagID
            WHERE AT.UserID = ?""",
            (userID,)
        )

    def getWithUserIDAndTagID(self, userID: int, tagID: int) -> Union[tuple, None]:
        """Gets an assigned tag with a userID and tagID."""
        return self.db.selectFirstWithParams(
            """SELECT * FROM AssignedTags WHERE UserID = ? AND TagID = ?""",
            (userID, tagID)
        )

    def insert(self, data: dict) -> None:
        """Inserts an assigned tag into the database."""
        self.db.execute(
            """INSERT INTO AssignedTags (TagID, UserID, Created) VALUES (?, ?, ?)""",
            (data["TagID"], data["UserID"], data["Created"])
        )
