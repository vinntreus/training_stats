import datetime

from web.app import app, db
from web.models import User


def create_tables():
    db.create_all()


def add_test_users():
    find_or_create_user('Test', 'Testsson', 'test@test.com', 'Password1')


def find_or_create_user(first_name, last_name, email, password):
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User(email=email,
                    username=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=app.user_manager.hash_password(password),
                    active=True,
                    confirmed_at=datetime.datetime.utcnow())
        db.session.add(user)
        db.session.commit()
    return user
