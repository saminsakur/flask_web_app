from flask import Blueprint

auth = Blueprint(__name__, "views")

@auth.route('/login')
def login():
    return "login"

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/signup')
def sign_up():
    return "Sign up"