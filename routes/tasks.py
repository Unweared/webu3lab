from flask import jsonify, request
from models.task import TaskManager
from config import Config

def configure_task_routes(app):
    @app.route('/api/tasks', methods=['GET', 'POST'])
    def handle_tasks():
        if request.method == 'GET':
            user_id = request.args.get('user_id')
            tasks = TaskManager.handle_task_operation('get_tasks', user_id)
            return jsonify({'tasks': tasks, 'status': 'success'})
        
        elif request.method == 'POST':
            data = request.get_json()
            success = TaskManager.handle_task_operation('create_task', 
                data['user_id'], 
                task_text=data['task_text']
            )
            return jsonify({'status': 'success' if success else 'error'})

    @app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
    def handle_single_task(task_id):
        user_id = request.json.get('user_id')
        
        if request.method == 'PUT':
            success = TaskManager.handle_task_operation('update_task',
                user_id,
                task_id=task_id,
                completed=request.json.get('completed')
            )
        
        elif request.method == 'DELETE':
            success = TaskManager.handle_task_operation('delete_task',
                user_id,
                task_id=task_id
            )
        
        return jsonify({'status': 'success' if success else 'error'})