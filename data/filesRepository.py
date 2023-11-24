from data.dataHelper import DataHelper

class FilesRepository:
    self.db = DataHelper()

    def getFileWithID(self, id: int):
        return self.db.selectFirstWithParams("SELECT * FROM Files WHERE FileID = ?;", (id,))



    def insert(self, data: dict):
        self.db.execute("""
        INSERT INTO files (FileID, Name, Extension, Description, Created)
            VALUES (?, ?, ?, ?, ?)
        """,
        (data["FileID"], data["Name"], data["Extension"], data["Description"], data["Created"])
        )