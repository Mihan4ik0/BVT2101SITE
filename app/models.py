from main import db


# Таблица для данных студентов
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)


# Таблица расписания занятий
class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(15), nullable=False)
    room = db.Column(db.String(20))
    form = db.Column(db.String(5), nullable=False)
    type = db.Column(db.String(3), nullable=False)
    even = db.Column(db.String(9), nullable=False)
    tutor_ti = db.relationship('Tutors')
    date_ti = db.relationship('Dates')
    day_ti = db.relationship('Days')
    subject_ti = db.relationship('Subjects')


# Таблица домашек по предметам
class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text(1000))
    file = db.Column(db.Varbinary(max), nullable=False)
    tutor_ho = db.relationship('Tutors')
    date_ho = db.relationship('Dates')
    day_ho = db.relationship('Days')
    subject_ho = db.relationship('Subjects')
    check_ho = db.relationship('Checks')


# Таблица инфо для студентов
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.Text(2000), nullable=False)
    date_ne = db.relationship('Dates')
    check_ne = db.relationship('Checks')


# Таблица с Фио преподователей
class Tutors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ti_tutor = db.Column(db.Integer, db.ForeignKey('timetable.id'))
    id_ho_tutor = db.Column(db.Integer, db.ForeignKey('homework.id'))
    tutor = db.Column(db.String(70))


# Таблица для дат (ч/м/г)
class Dates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ti_date = db.Column(db.Integer, db.ForeignKey('timetable.id'))
    id_ho_date = db.Column(db.Integer, db.ForeignKey('homework.id'))
    id_ne_date = db.Column(db.Integer, db.ForeignKey('news.id'))
    date = db.Column(db.Date, nullable=False)


# Таблица для дней недели
class Days(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ti_day = db.Column(db.Integer, db.ForeignKey('timetable.id'))
    id_ho_day = db.Column(db.Integer, db.ForeignKey('homework.id'))
    day = db.Column(db.String(20), nullable=False)


# Таблица для названий предметов
class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ti_subj = db.Column(db.Integer, db.ForeignKey('timetable.id'))
    id_ho_subj = db.Column(db.Integer, db.ForeignKey('homework.id'))
    subject = db.Column(db.String(70), nullable=False)


# Таблица проверки инфо админом
class Checks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ne_check = db.Column(db.Integer, db.ForeignKey('news.id'))
    id_ho_check = db.Column(db.Integer, db.ForeignKey('homework.id'))
    check = db.Column(db.Boolean, nullable=False)   # 0 - модерация, 1 - проверено

