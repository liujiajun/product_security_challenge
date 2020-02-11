# Zendesk Product Security
### The Zendesk Product Security Challenge
This authentication demo app is built for the **Zendesk Product Security Challenge**. It supports login, logout, and creating users. It is built on Flask and uses a simple json file to store data.

# Setup
To get started, you need to have **Python 3** installed on your computer. Although not required, it is recommended to use **Virtualenv** for isolated Python environment. 
- Clone this repository
- Initialize virtual environment and install dependencies:
  
  ```
  python3 -m venv app
  source app/bin/activate
  cd app
  pip install -r requirements.txt
  ```
- Use sample database:
  ```
  cp db_dev.json db.json
  ```
- Start the server in HTTP mode:
  ```
  python -m flask run 
  ```
  The server will be started on http://localhost:5000
- Alternatively, start the server in HTTPS mode:
  ```
  python -m flask run --cert cert.pem --key key.pem
  ```
  The server will be started on https://localhost:5000

If you are using the sample database, you can login in with the following credentials:
User name | Password
------------ | -------------
alice | 1234Abcd!
bob | 1234Abcd!
# Quick checklist
- [x] Input sanitization and validation
- [x] Password hashed
- [x] Prevention of timing attacks
- [ ] Logging
- [x] CSRF prevention
- [ ] Multi factor authentication
- [ ] Password reset / forget password mechanism
- [ ] Account lockout
- [x] Cookie
- [x] HTTPS
- [ ] Known password check

# Features
## Basic features
The app supports login, logout, and creating users. It also supports the Remember me option.
## Input sanitization and validation
User input is validated on both server side and client side
## Password hashed
All passwords are stored after then having been salted and hashed.
## CSRF prevention
All forms in the app are CSRF protected.
## Cookie
Cookies are used for the Remember Me feature.
## HTTPS
A self-signed certificate is added to support HTTPS.