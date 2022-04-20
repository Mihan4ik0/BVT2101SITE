from main import app
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user
from models import Users


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    if request.method == 'POST':
        email = Users.query.filter_by(email=request.form.get('login')).first()
        if email is None or not request.form.get('password') == email.password:
            return redirect(url_for('login'))
        login_user(email)
        return redirect(url_for('news'))
    return render_template('login.html')


@app.route('/reset')
def reset():
    return render_template("forgot_password.html")


@app.route('/update')
def update():
    return render_template("update_password.html")


@app.route('/news')
def news():
    return render_template("news.html")
