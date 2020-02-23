import psycopg2
from discord.ext import commands

class PostgresqlManager:

    def connect(self, database_url: str):
        self._conn = psycopg2.connect(database_url, sslmode="require")

    def cursor_connect(self):
        if self._conn is not None:
            if (
                not hasattr(self, "_cursor")
                or self._cursor is None
                or self._cursor.closed
            ):
                self._cursor = self._conn.cursor()

    def disconnect(self):
        if hasattr(self, "_cursor") and self._cursor is not None:
            self._cursor.close()
        if self._conn is not None:
            self._conn.close()

    def select(self, select : str, from_tables : str, where : str, end_of_sql_request : str ):
        if where == "":
            where = "TRUE"
        
        sql = ("SELECT " + select +
        " FROM " + from_tables +
        " WHERE " + where +
        end_of_sql_request
        )
        # add the 'server id' field

        self.cursor_connect()
        self._cursor.execute(sql)
        return self._cursor.fetchall()