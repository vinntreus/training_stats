from os import environ
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask('training_stats')
app.config.from_object(environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from training_stats.models import Workout


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
