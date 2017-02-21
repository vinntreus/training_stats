from datetime import date
from training_stats.models.workout import Workout, Exercise, Workouts
import pytest


def test_workout_init_date():
    workout = Workout(date=date(2017, 1, 1))
    assert workout.date == date(2017, 1, 1)


def test_workout_raise_without_date():
    with pytest.raises(TypeError):
        Workout()


def test_workout_with_exercise():
    workout = Workout(date=date(2017, 1, 1))
    workout.add_exercise(name='Knäböj', reps=8, weight=100)
    workout.add_exercise(name='Knäböj', reps=8, weight=101)
    assert workout.exercises == [
        Exercise(name='Knäböj', reps=8, weight=100),
        Exercise(name='Knäböj', reps=8, weight=101),
    ]


def test_workout_no_total_weight():
    workout = Workout(date=date(2017, 1, 1))
    assert workout.total_weight() == 0


def test_workout_total_weight_sums_weight():
    workout = Workout(date=date(2017, 1, 1))
    workout.add_exercise(name='a', reps=1, weight=1)
    assert workout.total_weight() == 1
    workout.add_exercise(name='a', reps=1, weight=1)
    assert workout.total_weight() == 2


def test_workout_total_weight_sums_weight_and_reps():
    workout = Workout(date=date(2017, 1, 1))
    workout.add_exercise(name='a', reps=2, weight=1)
    assert workout.total_weight() == 2
    workout.add_exercise(name='a', reps=1, weight=1.2)
    assert workout.total_weight() == 3.2


def test_workouts_total_weight_by_date_series():
    workouts = Workouts()

    w2 = Workout(date=date(2017, 1, 2))
    w2.add_exercise(name='a', reps=2, weight=1)
    workouts.add_workout(w2)

    w1 = Workout(date=date(2017, 1, 1))
    w1.add_exercise(name='a', reps=1, weight=1)
    workouts.add_workout(w1)

    assert workouts.total_weight_by_date_series() == [
        (date(2017, 1, 1), 1),
        (date(2017, 1, 2), 2)
    ]
