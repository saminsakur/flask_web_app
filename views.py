from flask import Blueprint

views = Blueprint(__name__, "views")

@views.route('/')
def get_home():
    return "<h1>Hello world!!!</h1>"