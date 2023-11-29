from data.dataHelper import DataHelper

class FilesRepository:
    def __init__(self):
        # Inherit the DataHelper class
        self.db = DataHelper()

    def insert(self, data: dict):
        """Inserts an account into the database."""
        self.db.execute(
            """INSERT INTO Files (FileID, Name, Extension, Description, Created) VALUES 
            (?, ?, ?, ?, ?)""",
            (data["FileID"], data["Name"], data["Extension"], data["Description"], data["Created"])
        )