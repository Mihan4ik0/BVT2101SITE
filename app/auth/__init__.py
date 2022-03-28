from flask import Blueprint

bp = Blueprint('auth', __name__)  # имя схемы элементов

from app.auth import routes
