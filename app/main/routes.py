from flask import render_template, redirect, request, flash
from flask.helpers import url_for

from app import db
from app.models import Users_req
from app.main import bp


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        username = request.form['username']
        phone = request.form['phone']

        if username == "" or phone == "":
            flash("Произошла ошибка")
            return redirect(url_for("main.form"))
        
        user = Users_req(username=username, phone=phone)

        db.session.add(user)
        db.session.commit()
        flash("Успешно записались, траляля, (app/main/routes.py line 30)")
        return redirect(url_for("main.index"))
    else:
        return render_template('form.html')


@bp.route('/photos')
def photos():
    return render_template('photos.html')


@bp.route('/contacts')
def contacts():
    return render_template('contacts.html')
