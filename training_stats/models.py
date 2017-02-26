from app import db
from sqlalchemy.dialects.postgresql import JSON, DATE


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(DATE, nullable=False)
    exercises = db.Column(JSON, nullable=False)

    def __init__(self, date, exercises):
        self.date = date
        self.exercises = exercises

    def __repr__(self):
        return '<id {}>'.format(self.id)
