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
        if hasattr(self, "_conn") and self._conn is not None:
            self._conn.close()

    # def select(self, select : str, from_tables : str, where : str, end_of_sql_request : str ):
    #     if where == "":
    #         where = "TRUE"

    #     sql = ("SELECT " + select +
    #     " FROM " + from_tables +
    #     " WHERE " + where +
    #     end_of_sql_request
    #     )
    #     # add the 'server id' field

    #     self.cursor_connect()
    #     self._cursor.execute(sql)
    #     return self._cursor.fetchall()

    def execute(self, sql):
        self.cursor_connect()
        cursor = (
            self._cursor
        )  # future: might create a self.get_new_cursor() function to multithreaded tasks ?
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)

        values = cursor.fetchall()
        # cursor.close() # for the future
        return values

    def insert(self, sql):
        self.cursor_connect()
        status = -1
        try:
            status = self._cursor.execute(sql)
        except Exception as e:
            print(e)

        self._conn.commit()
        return status
