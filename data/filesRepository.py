from data.dataHelper import DataHelper

class FilesRepository:
    db = DataHelper()

    def getFileWithID(id: int):
        return db.selectFirstWithParams("""
        SELECT files.fileID
        FROM files
        JOIN files.ID
        """, (id,))