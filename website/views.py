from .models import Note
from flask import Blueprint, render_template
from flask.globals import request
from flask.helpers import flash
from flask_login import login_required, current_user
from . import db


views = Blueprint(__name__, "views")


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(user_id=current_user.id, data=note)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)
