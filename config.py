import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'venv'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fucking-Frolovichev-and-Kunc'  # криптографический ключ
    SQLALCHEMY_DATABASE_URI = 'sqlite:///stud_ws.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['miha23112003@gmail.com']
    POSTS_PER_PAGE = 25  # элементов на странице
