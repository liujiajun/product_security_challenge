import re
import bcrypt
import config
salt = config.SALT

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


def validate(username, password):
    is_valid_username = re.search('''[a-z0-9]+''', username) is not None
    is_valid_password = re.search('''^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$''',
                                  password) is not None
    return is_valid_password and is_valid_username
