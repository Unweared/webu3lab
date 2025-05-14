from .connector import DatabaseConnector
from config import Config

class DatabaseInitializer:
    @staticmethod
    def initialize_databases():
        # Инициализация MariaDB
        mariadb_success = DatabaseInitializer._initialize_mariadb()
        sqlite_success = DatabaseInitializer._initialize_sqlite()
        
        return mariadb_success or sqlite_success

    @staticmethod
    def _initialize_mariadb():
        try:
            connector = DatabaseConnector('mariadb', Config.DATABASES['mariadb'])
            with connector.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(255) UNIQUE NOT NULL
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user_id INT NOT NULL,
                        task_text TEXT NOT NULL,
                        completed BOOLEAN DEFAULT FALSE,
                        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                    )
                """)
                conn.commit()
            return True
        except Exception as e:
            print(f"MariaDB initialization error: {str(e)}")
            return False

    @staticmethod
    def _initialize_sqlite():
        try:
            connector = DatabaseConnector('sqlite', Config.DATABASES['sqlite'])
            with connector.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        task_text TEXT NOT NULL,
                        completed INTEGER DEFAULT 0,
                        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                    )
                """)
                conn.commit()
            return True
        except Exception as e:
            print(f"SQLite initialization error: {str(e)}")
            return False