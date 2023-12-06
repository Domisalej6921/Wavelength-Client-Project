from data.dataHelper import DataHelper
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

    def getCommunity(self, name: str, wantName: bool):
        """Get a community name or ID via the name."""

        if wantName:
            return self.db.selectFirstWithParams(
                "SELECT Name FROM Entities WHERE Name = ?",
                (name,)
            )
        elif not wantName:
            return self.db.selectWithParams(
                "SELECT EntityId FROM Entities WHERE Name = ?",
                (name,)
            )
        else:
            return "Invalid input"


    def getCommunitiesSimilar(self, searchTerm: str):
        """Gets communities that have names like the search term."""
        return self.db.selectWithParams(
            "SELECT * FROM Entities WHERE Name LIKE ?",
            ("%" + searchTerm + "%",)
        )