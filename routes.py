# -*- coding: utf8 -*-
import random
from main import app, db, mail
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from models import Users, News, Timetable, Dates
from flask_mail import Message


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
        password = ''
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


@login_required
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        if current_user.password == request.form.get('old_password') and request.form.get('n_password1') == request.form.get('n_password2'):
            current_user.password = request.form.get('n_password1')
            db.session.commit()
            return redirect('news')
    return render_template("update_password.html")


@login_required
@app.route('/news')
def news():
    posts = db.session.query(Dates, News).join(Dates).order_by(Dates.date.desc()).all()
    return render_template("news.html", posts=posts)


@login_required
@app.route('/tt_home')
def tt_home():
    return render_template("timetable_homework.html")


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_required
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form.get('begin')
        date.split('-').reverse()
        date = ''.join(date)
        daty = db.session.query(Dates).filter(Dates.date == date).all()
        if '1' == request.form.get('category'):
            base = db.session.query(Dates, News).join(Dates).filter(Dates.date == date).all()
            i = 0
            r = 0
            while r != 1:
                try:
                    if base[i].Dates.id == daty[i].id:
                        i = i + 1
                    else:
                        r = 1
                        post = News(info=request.form.get('body'))
                        daty[i].merge(post)
                        db.session.add(post)
                        # db.session.add(data)
                        db.session.commit()
                except:
                    r = 1
                    post = News(info=request.form.get('body'))
                    data = Dates(date=date)
                    post.date_ne.append(data)
                    db.session.add(post)
                    db.session.add(data)
                    db.session.commit()
            return redirect('news')
        if '2' == request.form.get('category'):
            # base = db.session.query(Dates, Timetable).join(Dates).filter(Dates.date == date).all()
            # i = 0
            # r = 0
            # while r != 1:
            #     try:
            #         if base[i].Dates.id == daty[i].id:
            #             i = i + 1
            #         else:
            #             r = 1
            #             data = daty[i]
            #             if request.form.get('title').lower() == base[i]:
            #                 post = Timetable(homework=request.form.get('body'))
            #                 post.date_ne.append(data)
            #                 db.session.add(post)
            #                 db.session.add(data)
            #                 db.session.commit()
            #     except LookupError:
            #         r = 1
            #         post = Timetable(homework=request.form.get('body'))
            #         data = Dates(date=date)
            #         post.date_ne.append(date)
            #         db.session.add(post)
            #         db.session.add(data)
            #         db.session.commit()
            return redirect('news')
    return render_template("add_information.html")


@login_required
@app.route('/main')
def main():
    posts = db.session.query(Dates, News).join(Dates).order_by(Dates.date.desc()).all()
    timetable = db.session.query(Dates, Timetable).join(Dates).all()
    return render_template("main_page.html", posts=posts, timetable=timetable)
