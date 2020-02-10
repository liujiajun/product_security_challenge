from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from tinydb import TinyDB

from auth import auth as auth_blueprint
from config import SECRET_KEY, DATABASE_PATH, ENABLE_HTTPS, HTTPS_CERT_PATH, HTTPS_KEY_PATH
from main import main as main_blueprint
from user import User

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

CsrfProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(name):
    return User.get_user(name)


app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

db = TinyDB(DATABASE_PATH)

if __name__ == '__main__':
    if not ENABLE_HTTPS:
        app.run(ssl_context = (HTTPS_KEY_PATH, HTTPS_CERT_PATH))
    else:
        app.run()
