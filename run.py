from app import create_app,db
from app.models.user import User

app = create_app()
with app.app_context():
    existing_user= User.query.filter_by(username='admin').first()
    if existing_user:
        print("user already exists")
    else:
        user = User(username='admin')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)