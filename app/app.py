import sys
import os
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from tinydb import TinyDB

from auth import auth as auth_blueprint
from config import SECRET_KEY, DATABASE_PATH
from main import main as main_blueprint
from user import User

# To genrate binary file, set folders correspondingly.
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    cert_folder = os.path.join(sys._MEIPASS, 'cert')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    cert_folder = 'cert'
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
    app.run(ssl_context=(os.path.join(cert_folder, 'cert.pem'),
                         os.path.join(cert_folder, 'key.pem')))

# pyinstaller --onefile --add-data 'templates:templates' --add-data 'static:static' --add-data 'cert:cert' app.py