from flask import render_template, flash, redirect, url_for, request, current_app
from app.main import bp
from flask_login import login_required


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():  # логика главной страницы
    return render_template('index.html')
