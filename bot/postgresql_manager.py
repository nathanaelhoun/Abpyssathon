import psycopg2


class PostgresqlManager:
    """Easier access to the posgresql database linked with the bot"""

    def __init__(self):
        self._conn = None
        self._cursor = None

    def connect(self, database_url: str):
        """Connect to the database and store it"""
        self._conn = psycopg2.connect(database_url, sslmode="require")

    def cursor_connect(self):
        """Connect the cursor of the database and store it"""
        if self._conn is not None:
            if (
                not hasattr(self, "_cursor")
                or self._cursor is None
                or self._cursor.closed
            ):
                self._cursor = self._conn.cursor()

    def disconnect(self):
        """Disconnect the cursor and the database"""
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

    def execute(self, sql: str):
        """Execute a sql query and return the response"""
        self.cursor_connect()
        cursor = (
            self._cursor
        )  # future: might create a self.get_new_cursor() function to multithreaded tasks ?
        try:
            cursor.execute(sql)
        except psycopg2.Error as err:
            print(err)

        values = cursor.fetchall()
        # cursor.close() # for the future
        return values

    def insert(self, sql: str):
        """Execute an insert sql query and return the status"""
        self.cursor_connect()
        status = -1
        try:
            status = self._cursor.execute(sql)
        except psycopg2.Error as err:
            print(err)

        self._conn.commit()
        return status
