from flask import Blueprint

api = Blueprint("api", __name__)

from . import (
    cupons,
    deliveries,
    pontos_coleta,
    users,
)
