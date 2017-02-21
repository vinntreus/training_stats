from typing import List, Tuple
from datetime import date

class Exercise(dict):
    def __init__(self, name: str, reps: int, weight: float):
        self.name = name
        self.reps = reps
        self.weight = weight


class Workout:
    def __init__(self, date: date, exercises: List[Exercise] = None):
        self.date = date
        self.exercises = exercises or []

    def total_weight(self) -> float:
        return sum([e.weight * e.reps for e in self.exercises])


class Workouts:
    def __init__(self, workouts: List[Workout] = None):
        self.workouts = workouts or []

    def total_weight_by_date_series(self) -> List[Tuple[date, float]]:
        return sorted([(w.date, w.total_weight()) for w in self.workouts], key=lambda w: w[0])
