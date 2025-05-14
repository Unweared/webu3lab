import mariadb
import sqlite3
from typing import Union

class DatabaseConnector:
    def __init__(self, db_type: str, config: dict):
        self.db_type = db_type
        self.config = config
        self.connection = None

    def connect(self) -> Union[mariadb.Connection, sqlite3.Connection]:
        try:
            if self.db_type == 'mariadb':
                self.connection = mariadb.connect(**self.config)
            elif self.db_type == 'sqlite':
                self.connection = sqlite3.connect(self.config['database'])
            return self.connection
        except Exception as e:
            print(f"Connection error ({self.db_type}): {str(e)}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()