from flask import jsonify, request

from . import api
from app import db
from app.models import Usuario


@api.route("/user", methods=["POST"])
def get_user():
    request_data = request.get_json()
    cpf = request_data.get("cpf")
    if not(cpf):
        return jsonify(erro="Insira o CPF"), 400
    else:
        user = Usuario.query.filter_by(cpf=cpf)
        if not user:
            return jsonify(erro="Usuário não cadastrado")
        return jsonify(
            id = user.id,
            email = user.email,
            cpf = user.cpf,
            nome = user.nome,
            ecopoints = user.ecopoints
        )


@api.route("/user/<int:id>")
def get_user(id):
    user = Usuario.query.get_or_404(id)
    return jsonify(
        id = user.id,
        email = user.email,
        cpf = user.cpf,
        nome = user.nome,
        ecopoints = user.ecopoints
    )
