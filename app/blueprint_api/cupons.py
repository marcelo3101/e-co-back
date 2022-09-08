from datetime import datetime
from flask import jsonify, request

from . import api
from app import db
from app.models import Cupom, CupomResgatado, Usuario


@api.route("/get_cupons", methods=["GET"])
def cupons():
    cupons = Cupom.query.all()

    return jsonify([
        {
            "id": cupom.id,
            "nome": cupom.nome,
            "empresa": cupom.empresa,
            "descricao": cupom.descricao,
            "custo": cupom.custo,
            "data_validade": cupom.data_validade,
            "img": cupom.img
        } for cupom in cupons
    ])


@api.route("/redeem/<int:id>", methods=["POST"])
def redeem(id):
    """
        Resgatar cupom
    """
    cupom = Cupom.query.get_or_404(id)
    request_data = request.get_json()
    user = Usuario.query.get(request_data.get("user_id"))
    if not user:
        return jsonify(erro="Id do usuário faltando"), 400
    
    if db.session.query(db.exists().where(CupomResgatado.user_id == user.id, CupomResgatado.cupom_id == cupom.id)).scalar():
       return jsonify(message="Usuário já resgatou esse cupom")

    if cupom.data_validade < datetime.utcnow():
        return jsonify(erro="Cupom expirado")
    
    if cupom.custo > user.ecopoints:
        return jsonify(erro="Usuário não possui ecopoints suficientes")
    
    user.ecopoints = user.ecopoints - cupom.custo

    resgate = CupomResgatado(
        user_id=user.id,
        cupom_id=cupom.id
    )
    db.session.bulk_save_objects([resgate, user])
    db.session.commit()
    return jsonify(message="Cupom resgatado")