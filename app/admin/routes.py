import json
from flask import flash, json, redirect, render_template, url_for, jsonify, request
from flask_login import login_user, login_required, logout_user

from app import db
from app.admin import bp
from app.admin.forms import LoginForm

from app.models import Users_base, Users_req


@login_required
@bp.route('/users_req')
def users_req():
    requests = Users_req.query.filter_by(is_active=True).order_by(Users_req.username).all()
    return render_template('users_req.html', requests=requests)


@login_required
@bp.route("/decline", methods=["POST"])
def decline():
    data = json.loads(request.data)
    request_id = int(data["request_id"])
    user_request = Users_req.query.get(request_id)
    user_request.is_active = False
    db.session.add(user_request)
    db.session.commit()
    return jsonify({"status": "success"})


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.login.data
        password = form.password.data
        print(username)

        user = Users_base.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash("Неверный логин или пароль")
            redirect(url_for("admin.login"))
        else:
            login_user(user)
            return redirect(url_for("main.index"))
        
    return render_template("login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))