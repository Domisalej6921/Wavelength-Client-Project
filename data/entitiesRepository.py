from data.dataHelper import DataHelper

from typing import Union

class EntitiesRepository:

    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getCommunitiesOrdered(self, count: int):
        """Gets the first X communities to display."""
        return self.db.selectWithParams(
            "SELECT Name FROM Entities LIMIT ?",
            (count,)
        )

    def getCommunityReturnId(self, name: str):
        """Get a community id via the name."""
        return self.db.selectFirstWithParams(
            "SELECT EntityId FROM Entities WHERE Name = ?",
            (name,)
        )

    def getCommunityReturnName(self, name: str):
        """Get a community name via the name."""
        return self.db.selectFirstWithParams(
            "SELECT Name FROM Entities WHERE Name = ?",
            (name,)
        )


    def getCommunitiesSimilar(self, searchTerm: str):
        """Gets communities that have names like the search term."""
        return self.db.selectWithParams(
            "SELECT Name FROM Entities WHERE Name LIKE ?",
            ("%" + searchTerm + "%",)
        )

    def getIDWithProfilePictureID(self, profilePictureID: str) -> Union[tuple, None]:
        """Gets a community's ID with a profile picture ID."""
        return self.db.selectFirstWithParams("SELECT EntityID FROM Entities WHERE ProfilePictureID = ?", (profilePictureID,))

    def getReviewPageData(self) -> Union[list[tuple], None]:
        return self.db.select(
            """SELECT * FROM Entities Where isApproved = 0"""
        )

    def getWithEntityID(self, specificEntity: int) -> Union[list[tuple], None]:
        """Gets data for the selected entity."""
        return self.db.select("SELECT * FROM Entities WHERE EntityID = %s" % specificEntity)

    def insert(self, data: dict) -> None:
        """Inserts a community into the database."""
        self.db.execute(
            """INSERT INTO Entities (Name, Description, ProfilePictureID, BackgroundID, isCompany, isApproved, Created) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (data["Name"], data["Description"], data["ProfilePictureID"], data["BackgroundID"], data["isCompany"], data["isApproved"], data["Created"])
        )

    def DecisionAccept(self, specificEntity: int,) -> Union[list[tuple], None]:
        """Updates isApproved if the request has been accepted"""
        self.db.execute("UPDATE Entities SET isApproved = 1 WHERE EntityID = ?", (specificEntity, ))

    def DecisionDecline(self, specificEntity: int,) -> Union[list[tuple], None]:
        """Deletes community if the request has been declined"""
        self.db.execute("DELETE FROM Entities WHERE EntityID = ?", (specificEntity, ))
