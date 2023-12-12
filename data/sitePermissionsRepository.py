from typing import Union

from data.dataHelper import DataHelper

class SitePermissionsRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getWithID(self, UserID: int) -> Union[tuple, None]:
        """Gets a file from the database using its ID."""
        return self.db.selectFirstWithParams(
            """SELECT * FROM SitePermissions Where UserID = ?""",
            (UserID,)
        )
