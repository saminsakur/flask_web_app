from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route('/')
def get_home():
    return render_template("home.html")