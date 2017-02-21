from datetime import date

class Workouts:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def total_weight_by_date_series(self):
        return sorted([(w.date, w.total_weight()) for w in self.workouts], key=lambda w: w[0])

class Workout:
    def __init__(self, date: date):
        self.date = date
        self.exercises = []

    def add_exercise(self, name: str, reps: int, weight: float):
        self.exercises.append(Exercise(name, reps, weight))

    def total_weight(self):
        return sum([e.weight * e.reps for e in self.exercises])

class Exercise:
    def __init__(self, name: str, reps: int, weight: float):
        self.name = name
        self.reps = reps
        self.weight = weight

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)
