from sqlite3 import connect
from typing import Union

class DataHelper:
    def __init__(self, path: str = "data/databases/general.db"):
        self.conn = connect(path)
        self.cur = self.conn.cursor()

    def SelectFirst(self, query: str) -> Union[tuple, None]:
        """Selects one row from a query and returns it as a tuple."""
        self.cur.execute(query)
        return self.cur.fetchone()

    def SelectFirstWithParams(self, query: str, params: tuple) -> Union[tuple, None]:
        """Selects one row from a query using parameters and returns it as a tuple."""
        self.cur.execute(query, params)
        return self.cur.fetchone()

    def Select(self, query: str) -> Union[list[tuple], None]:
        """Selects all rows from a query and returns them as a list of tuples."""
        self.cur.execute(query)
        return self.cur.fetchall()

    def SelectWithParams(self, query: str, params: tuple) -> Union[list[tuple], None]:
        """Selects all rows from a query using parameters and returns them as a list of tuples."""
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def Execute(self, query: str, args: Union[tuple, None] = None) -> None:
        """Executes a query."""
        if args is not None:
            self.cur.execute(query, args)
        else:
            self.cur.execute(query)
        self.conn.commit()