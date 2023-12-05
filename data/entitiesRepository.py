from data.dataHelper import DataHelper
class EntitiesRepository:

    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getCommunity(self, name: str):
        """Get a community with the name."""
        return self.db.selectFirstWithParams(
            "SELECT EntityID, Name FROM Entities WHERE Name = ?",
            (name,)
        )

    def getCommunitiesSimilar(self, searchTerm: str):
        possibleCommunities = []
        possibleCommunities.append("SELECT * FROM Entities WHERE Name LIKE searchTerm")
        return possibleCommunities
