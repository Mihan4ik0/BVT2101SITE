# -*- coding: utf8 -*-
import random
from main import app, db, mail
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from models import Users
from flask_mail import Message
import js2py


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    if request.method == 'POST':
        email = Users.query.filter_by(email=request.form.get('login')).first()
        if email is None or not request.form.get('password') == email.password:
            return redirect(url_for('login'))
        login_user(email)
        return redirect(url_for('main'))
    return render_template('login.html')


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    if request.method == 'POST' and Users.query.filter_by(email=request.form.get('login')).first() is not None:
        email = request.form.get('login')
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        password =''
        for i in range(16):
            password += random.choice(chars)
        polzovatel = Users.query.filter_by(email=request.form.get('login')).first()
        polzovatel.password = password
        db.session.commit()
        msg = Message("Reset password", recipients=[email])
        msg.body = 'Ваш новый пароль: ' + password
        mail.send(msg)
        return redirect('login')
    return render_template("forgot_password.html")


@app.route('/update', methods=['GET', 'POST'])
def update():
    if current_user.is_authenticated:
        if request.method == 'POST':
            if current_user.password == request.form.get('old_password') and request.form.get('n_password1') == request.form.get('n_password2'):
                current_user.password = request.form.get('n_password1')
                db.session.commit()
                return redirect('news')
    return render_template("update_password.html")


@app.route('/news')
def news():
    return render_template("news.html")


@app.route('/tt_home')
def tt_home():
    return render_template("timetable_homework.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/add')
def add():
    return render_template("add_information.html")


@app.route('/main')
def main():
    return render_template("main_page.html")