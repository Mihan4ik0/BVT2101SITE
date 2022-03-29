from app import create_app, db
from app.models import Users, Timetable, Homework, News, Tutors, Dates, Days, Subjects, Checks


app = create_app()


if __name__ == "__main__":
    app.run()

