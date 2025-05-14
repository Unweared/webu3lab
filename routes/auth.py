from flask import jsonify, request
from models.user import UserManager
from config import Config

def configure_auth_routes(app):
    @app.route('/api/users', methods=['POST'])
    def handle_users():
        data = request.get_json()
        username = data.get('username', '').strip()
        
        if not username:
            return jsonify({'error': 'Username required'}), 400
        
        user_data = UserManager.create_or_get_user(username)
        Config.IN_MEMORY_STORAGE[user_data['id']] = []
        
        return jsonify({
            'user_id': user_data['id'],
            'username': user_data['username'],
            'status': 'success'
        })