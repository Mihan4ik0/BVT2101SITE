from datetime import datetime
from main import db


# Таблица для данных студентов
class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


# Таблица информации для студентов
class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    info = db.Column(db.Text(1000), nullable=False)
    date_ne = db.relationship('Dates')


# Таблица расписания занятий
class Timetable(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(3))
    room = db.Column(db.String(20))
    tutor = db.Column(db.String(70))
    day = db.Column(db.String(20), nullable=False)
    even = db.Column(db.String(9), nullable=False)
    subject = db.Column(db.String(70), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    homework = db.Column(db.String(1000), nullable=False)
    date_ti = db.relationship('Dates')


# Таблица для дат (ч/м/г)
class Dates(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date(), default = datetime.utcnow)
    id_ne_date = db.Column(db.Integer(), db.ForeignKey('news.id'))
    id_ti_date = db.Column(db.Integer(), db.ForeignKey('timetable.id'))
