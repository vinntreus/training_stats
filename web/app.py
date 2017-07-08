import json
from os import environ
from flask import Flask, render_template, redirect, url_for
from flask_user import login_required, UserManager, current_user
from web.models import db, load_workouts, get_workout, db_adapter, Workout
from web.forms import WorkoutForm


app = Flask(__name__)
user_manager = None
TITLE = 'Training stats'


def title(sub_title, title=TITLE):
    return '{sub_title} - {title}'.format(sub_title=sub_title, title=title)


def init_app(app, extra_config_settings={}):
    app.config.from_object(environ['APP_SETTINGS'])
    app.config.update(extra_config_settings)
    db.init_app(app)
    user_manager = UserManager(db_adapter, app)  # noqa: F841


def render(template, **kwargs):
    return render_template(template, **context(**kwargs))


def context(**kwargs):
    return dict(
        logo_text='Training stats',
        menu_items=[
            {'href': '/workouts', 'text': 'List workouts', 'css': ''},
            {'href': '/workouts/new', 'text': 'New workout', 'css': ''},
        ],
        **kwargs
    )


@app.route('/')
@login_required
def index():
    return render('index.html', title=TITLE)


@app.route('/workouts', methods=['GET'])
@login_required
def list_workouts():
    workouts = load_workouts(user_id=current_user.id)
    return render(
        'workouts_list.html',
        workouts=workouts,
        title=title('Workouts'),
    )


@app.route('/workouts/new', methods=['POST', 'GET'])
def create_workout():
    form = WorkoutForm()
    if form.validate_on_submit():
        if form.exercises.data:
            exercises = json.loads(form.exercises.data)
        else:
            exercises = None
        workout = Workout(date=form.date.data, exercises=exercises)
        workout.user_id = current_user.id
        db.session.add(workout)
        db.session.commit()
        return redirect(url_for('show_workout', workout_id=workout.id))
    else:
        return render(
            'workout_create.html',
            form=form,
            title=title('New workout'),
        )


@app.route('/workouts/<workout_id>', methods=['GET'])
def show_workout(workout_id):
    workout = get_workout(workout_id)
    return render(
        'workout_show.html',
        workout=workout,
        title=title('Workout'),
    )
