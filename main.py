from app import create_app, db
from app.models import Users, Timetable, Homework, News, Tutors, Dates, Days, Subjects, Checks


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Timetable' : Timetable, 'Homework' : Homework, 'News': News, 'Tutors': Tutors, 'Dates' : Dates, 'Days': Days, 'Subjects': Subjects, 'Checks' : Checks}
