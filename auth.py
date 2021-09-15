from flask import Blueprint, render_template

auth = Blueprint(__name__, "views")

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/signup')
def sign_up():
    return "Sign up"