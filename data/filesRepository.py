from typing import Union

from data.dataHelper import DataHelper

class FilesRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def getWithID(self, fileID: str) -> Union[tuple, None]:
        """Gets a file from the database using its ID."""
        return self.db.execute(
            """SELECT * FROM Files WHERE FileID = ?""",
            (fileID,)
        )

    def insert(self, data: dict) -> None:
        """Inserts an account into the database."""
        self.db.execute(
            """INSERT INTO Files (FileID, Name, Extension, Description, Created) VALUES 
            (?, ?, ?, ?, ?)""",
            (data["FileID"], data["Name"], data["Extension"], data["Description"], data["Created"])
        )

    def delete(self, fileID: str) -> None:
        """Deletes a file from the database using its ID."""
        self.db.execute(
            """DELETE FROM Files WHERE FileID = ?""",
            (fileID,)
        )