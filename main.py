# -*- coding: utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
import os

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stud_ws.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # адрес почты
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # адрес почты
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # пароль от почты почты
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)
login = LoginManager()
db.init_app(app)
login.init_app(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
