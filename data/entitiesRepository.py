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

    def getCommunity(self, name: str):
        """Get a community with the name."""
        return self.db.selectFirstWithParams(
            "SELECT EntityID, Name FROM Entities WHERE Name = ?",
            (name,)
        )

    def getCommunitiesSimilar(self, searchTerm: str):
        """Gets communities that have names like the search term."""
        return self.db.selectWithParams(
            "SELECT * FROM Entities WHERE Name LIKE ?",
            (searchTerm,)
        )