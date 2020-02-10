from flask import Flask
from tinydb import TinyDB
from flask_login import LoginManager
from auth import auth as auth_blueprint
from main import main as main_blueprint
from user import User
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(name):
    return User.get_user(name)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

db = TinyDB('db.json')

if __name__ == '__main':
    app.run()
