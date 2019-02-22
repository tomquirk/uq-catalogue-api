"""
Database Utility
"""

import psycopg2
from src.logger import get_logger

_LOG = get_logger("database")


class Db:
    """
    Mini wrapper for database interaction
    """

    def __init__(self):
        self._conn = None
        self._cursor = None

    def connect(self, dbname, username, password, host):
        """ Establishes connection with psql server
        """
        connect_str = "dbname='%s' user='%s' host='%s' password='%s'" % (
            dbname,
            username,
            host,
            password,
        )
        self._conn = psycopg2.connect(connect_str)
        self._cursor = self._conn.cursor()

    def select(self, query, data=None):
        """ execution suitable for read queries, returning the rows returned from given query.
        """
        _LOG.debug(f"exectuting:{query}")
        self._cursor.execute(query, data)
        return self._cursor.fetchall()

    def commit(self, query, data=None):
        """ execution suitable for update queries
        """
        _LOG.debug("exectuting:{query}")
        self._cursor.execute(query, data)
        self._conn.commit()

    def disconnect(self):
        """Closes database connection
        """
        self._conn.close()

