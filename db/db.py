import psycopg2

class Db:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def connect(self, dbname, username, password, host):
        """ Establishes connection with psql server
        """
        try:
            connect_str = "dbname='%s' user='%s' host='%s' password='%s'" % \
              (dbname, username, host, password)
            self._conn = psycopg2.connect(connect_str)
            self._cursor = self._conn.cursor()
        except Exception as e:
            print("Error connecting to database\n", e)

    def select(self, query):
        """ execution suitable for read queries, returning the rows returned from given query.
        """
        print("Exectuting ", query)
        self._cursor.execute(query)
        return self._cursor.fetchall()

    def commit(self, query):
        """ execution suitable for update queries
        """
        print("Exectuting ", query)
        self._cursor.execute(query)
        self._conn.commit()

    def disconnect(self):
        """Closes database connection
        """
        self._conn.close()
        