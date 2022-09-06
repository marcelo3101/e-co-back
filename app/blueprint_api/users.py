from flask import jsonify

from . import api
from app import db
from app.models import Usuario
@api.route("/user", methods=["POST"])
def get_)user():
    request_data = request.get_json()
    user_id = request_data.get("user_id")
    if not(user_id):
        return jsonify(erro="Insira o CPF"), 400
    else:
        user = Usuario.query.filter_by(id=user_id)
        return jsonify(
            id= user.id,
            email = user.email,
            nome = user.nome,
            ecopoints = user.ecopoints
        )