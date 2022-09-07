from flask import jsonify, request

from . import api
from app import db
from app.models import Entrega, Usuario

api.route("/delivery", methods=["POST"])
def create_delivery():
    """
        Método para criar entregas
        -----
        parameters:
            - JSON
                - user_id
                - ponto_coleta_id
                - nome_produto
                - categoria
    """
    request_data = request.get_json()
    ponto_coleta_id = request_data.get("ponto_coleta_id")
    nome_produto = request_data.get("nome_produto")
    categoria = request_data.get("categoria")
    if not (
        ponto_coleta_id and
        nome_produto and
        categoria
    ):
        return jsonify(erro="Parâmetros faltando"), 400
    entrega = Entrega(
        ponto_coleta=ponto_coleta_id,
        nome_produto=nome_produto,
        categoria=categoria,
        estado=1
    )
    db.session.add(entrega)
    db.session.commit()
    return jsonify(
        id=entrega.id,
        usuario = entrega.usuario,
        ponto_coleta=entrega.ponto_coleta,
        nome_produto=entrega.nome_produto,
        categoria=entrega.categoria,
        estado=entrega.estado
    ), 201


api.route("/delivery/confirm/<int:id>")  # Rota para simular a confirmação de uma entrega
def confirm_delivery(id):
    """
        Rota que simula o scan do qrcode para confirmação da entrega
        Garante +600 ecopoints
        -----
        parameters:
            - JSON:
                - user_id
    """
    entrega: Entrega = Entrega.query.get_or_404(id)
    if entrega.estado != 1:
        return jsonify(erro="Estado da entrega inválido"), 400

    request_data = request.get_json()
    user_id = request_data.get("user_id")
    if not user_id:
        return jsonify(erro="Id do usuário faltando"), 400
    
    entrega.pontuacao = 600
    entrega.usuario = user_id
    usuario: Usuario = Usuario.query.get(user_id)
    usuario.ecopoints += 600
    db.session.bulk_save_objects([entrega, usuario])
    return jsonify(message="Entrega confirmada"), 200

    