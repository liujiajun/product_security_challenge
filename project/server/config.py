import os

SECRET_KEY = os.environ.get('ZENDESK_CHALLENGE_SECRET_KEY') or 'fa2c5f7ba0e17f7a897459ba'

SALT = os.environ.get('ZENDESK_CHALLENGE_SALT') or b'$2b$12$6MhgwN.6B3MIeFwTtHWSIe'

DATABASE_PATH = 'db.json'

ENABLE_HTTPS = True
HTTPS_CERT_PATH = 'cert.pem'
HTTPS_KEY_PATH = 'key.pem'
