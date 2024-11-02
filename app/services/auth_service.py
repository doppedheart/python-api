from app.models.user import User
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        print(user)
        if user and user.check_password(password):
            return create_access_token(identity=user.id)
        return None