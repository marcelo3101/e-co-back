from flask import jsonify

from . import api

@api.route("/test")
def test():
    return jsonify(message="Funcionando")