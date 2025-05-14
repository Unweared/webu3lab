from database.connector import DatabaseConnector
from config import Config

class UserManager:
    @staticmethod
    def create_or_get_user(username: str):
        user_data = None
        for db_type in ['mariadb', 'sqlite']:
            connector = DatabaseConnector(db_type, Config.DATABASES[db_type])
            with connector.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
                user = cursor.fetchone()
                
                if not user:
                    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
                    conn.commit()
                    user_id = cursor.lastrowid
                else:
                    user_id = user[0]
                
                if not user_data:
                    user_data = {'id': user_id, 'username': username}
        
        return user_data