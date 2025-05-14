from database.connector import DatabaseConnector
from config import Config

class TaskManager:
    @staticmethod
    def handle_task_operation(operation: str, user_id: int, **kwargs):
        results = []
        for db_type in ['mariadb', 'sqlite']:
            connector = DatabaseConnector(db_type, Config.DATABASES[db_type])
            with connector.connect() as conn:
                try:
                    result = getattr(TaskManager, f"_{operation}")(conn, user_id, **kwargs)
                    results.append(result)
                except Exception as e:
                    print(f"Error in {operation} operation ({db_type}): {str(e)}")
        return any(results)

    @staticmethod
    def _create_task(conn, user_id, task_text):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (user_id, task_text) VALUES (?, ?)",
            (user_id, task_text)
        )
        conn.commit()
        return True

    @staticmethod
    def _get_tasks(conn, user_id):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, task_text, completed FROM tasks WHERE user_id = ?",
            (user_id,)
        )
        return [
            {'id': t[0], 'text': t[1], 'completed': bool(t[2])}
            for t in cursor.fetchall()
        ]

    @staticmethod
    def _update_task(conn, user_id, task_id, completed):
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET completed = ? WHERE id = ? AND user_id = ?",
            (completed, task_id, user_id)
        )
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def _delete_task(conn, user_id, task_id):
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        conn.commit()
        return cursor.rowcount > 0