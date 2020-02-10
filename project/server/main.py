from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('auth.login'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
