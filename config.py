class Config:
    DATABASES = {
        'mariadb': {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'task_manager'
        },
        'sqlite': {
            'database': 'tasks_sqlite.db'
        }
    }
    
    IN_MEMORY_STORAGE = {}