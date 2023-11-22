from sqlite3 import connect

class DataHelper:
    def __init__(self, path: str = "data/databases/general.db"):
        self.conn = connect(path)
        self.cur = self.conn.cursor()

    def SelectFirst(self, query: str) -> tuple:
        """Selects one row from a query and returns it as a tuple."""
        self.cur.execute(query)
        return self.cur.fetchone()

    def SelectFirstWithParams(self, query: str, params: tuple) -> tuple:
        """Selects one row from a query using parameters and returns it as a tuple."""
        self.cur.execute(query, params)
        return self.cur.fetchone()

    def Select(self, query: str) -> list[tuple]:
        """Selects all rows from a query and returns them as a list of tuples."""
        self.cur.execute(query)
        return self.cur.fetchall()

    def SelectWithParams(self, query: str, params: tuple) -> list[tuple]:
        """Selects all rows from a query using parameters and returns them as a list of tuples."""
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def Execute(self, query: str) -> None:
        """Executes a query."""
        self.cur.execute(query)
        self.conn.commit()