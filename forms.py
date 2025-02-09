from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, EmailField
from wtforms.validators import InputRequired



class GetProblem(FlaskForm):
    
    username = StringField('Name', validators=[InputRequired()])
    office_number = StringField('office_number', validators=[InputRequired()])
    department = StringField('department', validators=[InputRequired()])
    problem = TextAreaField('problem', validators=[InputRequired() ])
    
    
    
class LogIn(FlaskForm):
    
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    


class NewUser(FlaskForm):
    
    firstname = StringField('First Name', validators=[InputRequired()])
    surname = StringField('Last Name', validators=[InputRequired()])
    useremail = EmailField('User email', validators=[InputRequired()])
    system_role = SelectField('Choose role', choices=['Administrator','General User'], validators=[InputRequired()])
    position = StringField('Work Position', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    