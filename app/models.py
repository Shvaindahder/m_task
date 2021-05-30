from datetime import datetime
from flask_login.mixins import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class Users_req(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    date_of_request = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'Имя: {self.username}'


class Users_base(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return Users_base.query.get(int(id))
