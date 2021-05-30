import click
from project import app

from app import db
from app.models import Users_base


@app.cli.group()
def user():
    pass


@user.command()
@click.argument('username')
@click.argument('password')
def createsuperuser(username, password):
    user = Users_base(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

