from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm): #Вход в учётную запись
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ResetPasswordRequestForm(FlaskForm): #Восстановление пароля
    email= StringField('Email', validators= [DataRequired(), Email()])
    submit= SubmitField('Request Password Reset')

class resetPasswordForms(FlaskForm):
    password= PasswordField('Password', validators=[DataRequired()])
    password2= PasswordField(
        'Repeat Password', validators=[DataRequired(), ('passsword')])
    submit= SubmitField('Request Password Reset')