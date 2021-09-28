from flask.globals import request
from flask.templating import render_template
from flask.helpers import flash, url_for
from flask.blueprints import Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint(__name__, "views")


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists!", category="error")
        elif len(email) < 4:
            flash("Email must me greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must me greater than 4 characters.", category="error")
        elif password1 != password2:
            flash("Passwords doesn't match", category="error")
        elif len(password1) <= 5:
            flash("Password must me at least 6 characters long", category="error")
        else:
            usr = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="sha256"),
            )
            db.session.add(usr)
            db.session.commit()
            login_user(usr, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("website.views.home"))

    return render_template("signup.html", user=current_user)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("website.views.home"))

            else:
                flash("Incorrect password, please try again", category="error")
        else:
            flash("Email does not exists!", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("website.auth.login"))
