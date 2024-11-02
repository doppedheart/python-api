from app.services.auth_service import AuthService
from flask import jsonify

class AuthController:
    @staticmethod
    def login(data):
        token = AuthService.authenticate_user(data.get('username'), data.get('password'))
        print(token)
        if token:
            return jsonify({'access_token': token}), 200
        return jsonify({'error': 'Invalid credentials'}), 401
