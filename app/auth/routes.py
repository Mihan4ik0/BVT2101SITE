from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, \
    ResetPasswordRequestForm, ResetPasswordForm
from app.models import Users
from app.auth.email import send_password_reset_email


@bp.route('/login', methods=['GET', 'POST'])  # отлавливание страницы логина
def login():   # логика страницы входа
    if current_user.is_authenticated:  # проверка пользователя на регистрацию
        return redirect(url_for('main.index'))  # перенаправление на главную
    form = LoginForm()  # создание формы логина
    if form.validate_on_submit():  # проверка на запрос POST
        user = Users.query.filter_by(username=form.username.data).first()  # запрос пользователя из БД
        if user is None or not user.check_password(form.password.data):  # проверка пароля
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)  # регистрирование входа пользователя, если данные верны
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():  # логика страницы  выхода
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/reset_password_request', methods=['GET','POST'])
def reset_password_request():  # логика запроса на сброс пароля
    if current_user.is_authenticated:  # проверка авторизован ли пользователь
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():  # проверка на заполненность формы
        user = Users.query.filter_by(email=form.email.data).first()  # поиск соответствия почт из БД и в форме
        if user:
            send_password_reset_email(user)
            flash('Проверьте свою электронную почту для получения инструкций по сбросу пароля')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', title='Reset Password', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):  # логика сброса пароля
    if current_user.is_authenticated:  # проверка на авторизацию
        return redirect(url_for('main.index'))
    user = Users.verify_reset_password_token(token)
    if not user:
        return redirect((url_for('main.index')))
    form = ResetPasswordForm()
    if form.validate_on_submit():  # проверка формы на заполненность
        user.set_password(form.password.data)
        db.session.commit()
        flash('Ваш пароль был сброшен')
        return redirect(url_for('main.login'))
    return render_template('auth/reset_password.html', form=form)
