from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):  # создание формы входа пользователя
    username = StringField('Имя пользователя', validators=[DataRequired()])  # форма с проверкой на наполненность
    password = PasswordField('Пароль', validators=[DataRequired()])  # форма с проверкой на наполненность
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class ResetPasswordRequestForm(FlaskForm):  # форма запроса на сброс пароля
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    submit = SubmitField('Запросить Сброс Пароля')


class ResetPasswordForm(FlaskForm):  # форма сброса пароля
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сменить пароль')
