from app import create_app,db
from app.models.user import User

app = create_app()
with app.app_context():
    user = User(username='admin')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)