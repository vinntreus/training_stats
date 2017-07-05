from flask_wtf import FlaskForm
from wtforms import DateField, StringField
from wtforms.validators import DataRequired


class WorkoutForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    exercises = StringField('Exercises')
