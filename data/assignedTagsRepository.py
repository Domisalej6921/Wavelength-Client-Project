from typing import Union
from data.dataHelper import DataHelper

class AssignedTagsRepository:
    def init(self):
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