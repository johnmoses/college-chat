from flask import Blueprint

bp = Blueprint('college', __name__)

from college import routes
