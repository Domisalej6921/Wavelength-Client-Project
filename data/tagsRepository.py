from typing import Union

from data.dataHelper import DataHelper

class TagsRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def get(self) -> Union[list[tuple], None]:
        """Gets all tags from the database."""
        return self.db.select("SELECT * FROM Tags")

    def getWithID(self, tagID: int) -> Union[tuple, None]:
        """Gets a tag from the database with a tagID."""
        return self.db.selectFirstWithParams("SELECT * FROM Tags WHERE TagID = ?", (tagID,))

    def getWithUserID(self, userID: int) -> Union[list[tuple], None]:
        """Gets a tag from the database with a tagID."""
        return self.db.selectWithParams(
            """SELECT T.TagID, T.Name, T.Colour, T.Created 
            FROM Tags T
            INNER JOIN AssignedTags AT on T.TagID = AT.TagID
            WHERE AT.UserID = ?""",
            (userID,)
        )

    def getWithSearch(self, search: str) -> Union[list[tuple], None]:
        """Gets all tags from the database with a search and order it by the amount of users assigned to it."""
        return self.db.selectWithParams(
            """SELECT T.TagID, T.Name, T.Colour, T.Created, COUNT(AT.TagID)
            FROM Tags T
            INNER JOIN AssignedTags AT on T.TagID = AT.TagID
            WHERE Name LIKE ? ORDER BY COUNT(AT.TagID) DESC""",
            ("%" + search + "%",)
        )

    def insert(self, data: dict) -> None:
        """Inserts a tag into the database."""
        self.db.execute(
            """INSERT INTO Tags (CreatedBy, Name, Colour, Created) VALUES (?, ?, ?)""",
            (data["CreatedBy"], data["Name"], data["Colour"], data["Created"])
        )

    def delete(self, tagID: int) -> None:
        """Deletes a tag from the database."""
        # First delete any tag associations
        self.db.execute("DELETE FROM AssignedTags WHERE TagID = ?", (tagID,))

        # Then delete the tag
        self.db.execute("DELETE FROM Tags WHERE TagID = ?", (tagID,))