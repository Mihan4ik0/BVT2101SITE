from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)  # отлавливаем ошибку 404
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)  # отлавливаем ошибку 500
def internal_error(error):
    db.session.rollback()
    return render_template('errors/404.html'), 500
