from flask import Blueprint, render_template, request, flash, redirect, url_for, Markup
from flask_login import login_user, logout_user, login_required, current_user

import utils
from user import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    if not utils.validate(username, password):
        flash('Invalid username or password')
        return redirect(url_for('auth.login'))

    if not User.verify_user(username, password):
        flash('Invalid username or password')
        return redirect(url_for('auth.login'))

    login_user(User(username, password), remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    name = request.form.get('username')
    password = request.form.get('password')

    if not utils.validate(name, password):
        flash(Markup(
            "Username should contain only lower case letters and/or numbers. </br> Password should have no less than 8"
            " characters, and contain"
            "at least one of each: 1) lower case letters; 2) upper case letters; 3) numbers; 4) special characters"))
        return redirect(url_for('auth.signup'))

    if not User.add_user(name, password):
        flash(Markup("Username already exists. Go to <a href=" + url_for('auth.login') + ">login page</a>"))
        return redirect(url_for('auth.signup'))

    flash("Sign up success")
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
