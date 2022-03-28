from flask import Blueprint

bp = Blueprint('errors', __name__)  # имя схемы элементов

from app.errors import handlers
