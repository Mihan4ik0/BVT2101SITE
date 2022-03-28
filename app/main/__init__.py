from flask import Blueprint

bp = Blueprint('main', __name__)  # имя схемы элементов

from app.main import routes
