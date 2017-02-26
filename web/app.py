from os import environ
from flask import Flask, render_template, redirect, url_for
from web.models import db, load_workouts, get_workout

app = Flask(__name__)
app.config.from_object(environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html', title=title())


@app.route('/workouts', methods=['GET'])
def list_workouts():
    workouts = load_workouts()
    return render_template(
        'workouts_list.html',
        workouts=workouts,
        title=title('Workouts'),
    )


@app.route('/workouts', methods=['POST'])
def create_workout():
    # validate form
    # create workout from form
    # handle errors
    # redirect to workout-page
    return redirect(url_for('show_workout', workout_id=1))


@app.route('/workouts/<workout_id>', methods=['GET'])
def show_workout(workout_id):
    workout = get_workout(workout_id)
    return render_template(
        'workout_show.html',
        workout=workout,
        title=title('Workout'),
    )

def title(sub_title=None):
    title = 'Training stats'
    if sub_title:
        return '{sub_title} - {title}'.format(sub_title=sub_title, title=title)
    else:
        return title
