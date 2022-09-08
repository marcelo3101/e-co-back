from flask import jsonify, request

from . import api
from app.models import PontoColeta


@api.route("/pontos")
def get_pontos():
    pontos = PontoColeta.query.all()

    return jsonify([
        {
            "id": ponto.id,
            "nome": ponto.nome,
            "descricao": ponto.descricao,
            "endereco": ponto.endereco,
            "latitude": ponto.latitude,
            "longitude": ponto.longitude
        } for ponto in pontos
    ])