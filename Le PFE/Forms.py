from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length



class LoginForm(FlaskForm):
    login = StringField('login',validators=[DataRequired(),Length(min=2,max=20)])
    mdp = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me ') 
    submit = SubmitField('sign in')