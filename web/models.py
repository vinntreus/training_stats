from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON, DATE


db = SQLAlchemy()


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


def load_workouts():
    return [
        {
            'id': 1,
            'date': date(2017, 2, 26),
            'exercises': [
                {
                    'name': 'Marklyft',
                    'sets': [
                        {'reps': 10, 'weight': 120},
                        {'reps': 10, 'weight': 130},
                        {
                            'reps': 10,
                            'weight': 135,
                            'notes': 'Tappa grepp efter 6'
                        },
                    ]
                },
                {
                    'name': 'Chins',
                    'sets': [
                        {'reps': 10, 'weight': 0},
                        {'reps': 8, 'weight': 5},
                        {'reps': 6, 'weight': 5},
                    ]
                },
                {
                    'name': 'Militärpress',
                    'sets': [
                        {'reps': 10, 'weight': 50},
                        {'reps': 10, 'weight': 55},
                        {'reps': [4, 4, 4], 'weight': [60, 50, 40]},
                    ]
                },
            ]
        },
        {
            'id': 2,
            'date': date(2017, 2, 24),
            'exercises': [
                {
                    'name': 'Bänkpress',
                    'sets': [
                        {'reps': 10, 'weight': 80},
                        {'reps': 8, 'weight': 80},
                        {'reps': 10, 'weight': 75},
                    ]
                },
                {
                    'name': 'Knäböj',
                    'sets': [
                        {'reps': 10, 'weight': 70},
                        {'reps': 10, 'weight': 70},
                        {'reps': 10, 'weight': 70},
                    ]
                },
                {
                    'name': 'Skivstångsrodd',
                    'sets': [
                        {'reps': 10, 'weight': 60},
                        {'reps': 10, 'weight': 60},
                        {'reps': 10, 'weight': 60},
                    ]
                },
            ]
        }
    ]


def get_workout(workout_id):
    return load_workouts()[0]
