from typing import List
from datetime import date


def total_weight_by_date(workouts):
    return sorted(
        [(w.date, w.total_weight()) for w in workouts],
        key=lambda w: w[0]
    )


class Exercise(dict):
    def __init__(self, name: str, reps: int, weight: float):
        self.name = name
        self.reps = reps
        self.weight = weight


class Workout:
    def __init__(self, date: date, exercises: List[Exercise] = None):
        self.date = date
        self.exercises = exercises or []

    def total_weight(self):
        return sum([e.weight * e.reps for e in self.exercises])
