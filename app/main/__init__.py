from os import lseek

from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix='/main')

from app.main import routes