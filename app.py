from flask import Flask, render_template
from database.initializer import DatabaseInitializer
from routes.auth import configure_auth_routes
from routes.tasks import configure_task_routes

def create_app():
    app = Flask(__name__)
    
    # Инициализация баз данных
    if not DatabaseInitializer.initialize_databases():
        raise RuntimeError("Database initialization failed")
    
    # Главный маршрут
    @app.route('/')
    def index():
        return render_template('index.html')  # Рендеринг шаблона

    # Регистрация маршрутов для авторизации и задач
    configure_auth_routes(app)
    configure_task_routes(app)
    
    return app

  if __name__ == '__main__':
      app = create_app()
      app.run(host='0.0.0.0', port=5000, debug=True)

