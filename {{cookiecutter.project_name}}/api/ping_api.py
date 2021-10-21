from flask import Blueprint

from common.response import resp

ping_bp = Blueprint("ping", __name__)


@ping_bp.route("/ping")
def ping():
    return resp(data="pong")
