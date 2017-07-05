from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON, DATE
from flask_user import UserMixin, SQLAlchemyAdapter


db = SQLAlchemy()


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(DATE, nullable=False)
    exercises = db.Column(JSON, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date, exercises=None):
        self.date = date
        self.exercises = exercises or []

    def __repr__(self):
        return '<Workout id={}>'.format(self.id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # User information
    active = db.Column(
        'is_active',
        db.Boolean(),
        nullable=False,
        server_default='0',
    )
    first_name = db.Column(db.String(100), nullable=False, server_default='')
    last_name = db.Column(db.String(100), nullable=False, server_default='')
    workouts = db.relationship('Workout', backref='user', lazy='dynamic')


db_adapter = SQLAlchemyAdapter(db, User)


def get_workout(workout_id):
    return Workout.query.get(workout_id)


def load_workouts(user_id):
    q = Workout.query.filter(User.id == user_id)
    return q.order_by(Workout.date.desc())
