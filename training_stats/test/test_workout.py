from datetime import date
from training_stats.models.workout import Workout, Exercise, Workouts


def test_workout_without_exercises_has_zero_total_weight():
    workout = Workout(date=date(2017, 1, 1))
    assert workout.total_weight() == 0


def test_workout_total_weight_sums_weight_and_reps():
    workout = Workout(
        date=date(2017, 1, 1),
        exercises=[
            Exercise(name='a', reps=2, weight=1),
            Exercise(name='a', reps=1, weight=1.2),
        ]
    )
    assert workout.total_weight() == 3.2


def test_workouts_total_weight_by_date_series():
    workouts = Workouts(workouts=[
        Workout(date=date(2017, 1, 2), exercises=[
            Exercise(name='a', reps=2, weight=1),
        ]),
        Workout(date=date(2017, 1, 1), exercises=[
            Exercise(name='a', reps=1, weight=1),
        ])
    ])

    assert workouts.total_weight_by_date_series() == [
        (date(2017, 1, 1), 1),
        (date(2017, 1, 2), 2)
    ]
