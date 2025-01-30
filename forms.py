from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired



class GetProblem(FlaskForm):
    
    username = StringField('Name', validators=[InputRequired()])
    office_number = StringField('office_number', validators=[InputRequired()])
    department = StringField('department', validators=[InputRequired()])
    problem = TextAreaField('problem', validators=[InputRequired() ])
    
    
    
class LogIn(FlaskForm):
    
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
