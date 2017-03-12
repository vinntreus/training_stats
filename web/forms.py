from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import DataRequired

class WorkoutForm(FlaskForm):
    date = DateField('date', validators=[DataRequired()])
