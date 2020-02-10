from flask_login import UserMixin
from tinydb import Query

import app
import utils


class User(UserMixin):
    def __init__(self, name, hashed_password):
        self.name = name
        self.password = hashed_password

    def get_id(self):
        return self.name

    @staticmethod
    def add_user(name, password):
        User = Query()
        res = app.db.search(User.username == name)

        if res:
            return False

        app.db.insert({'username': name, 'password': utils.hash_password(password)})
        return True

    @staticmethod
    def verify_user(name, hashed_password):
        query = Query()
        res = app.db.search(query.username == name)
        if not res or not utils.verify_password(hashed_password, res[0]['password']):
            return False
        return True

    @staticmethod
    def get_user(name):
        query = Query()
        res = app.db.search(query.username == name)
        if not res:
            return None
        return User(res[0]['username'], res[0]['password'])
