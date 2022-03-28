from flask import render_template, flash, redirect, url_for, request, current_app
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
def index():  # логика главной страницы
    return render_template('index.html')
