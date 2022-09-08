from datetime import datetime
from app import create_app, db
from app.models import Cupom, Entrega, PontoColeta, Usuario

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command("dev_db")
def dev_db():
    db.drop_all()
    db.create_all()

    user = Usuario(
        cpf="00000000000",
        email="email@email.com",
        nome = "Usuário ECO",
        ecopoints = 500
    )

    ponto_coleta = PontoColeta(
        nome="Ponto de coleta UnB",
        descricao="Ponto de coleta de lixo eletrônico",
        endereco="https://www.openstreetmap.org/search?whereami=1&query=-15.76114%2C-47.86752#map=19/-15.76114/-47.86752",
        latitude="-15.76114",
        longitude="-47.86752"
    )

    cupom = Cupom(
        nome="Entrega grátis para qualquer pedido",
        empresa="Ifood",
        descricao="Faça seu pedido com entrega grátis para qualquer restaurante cadastrado!",
        custo=300,
        data_validade=datetime(2022, 12, 1),
        img="https://play-lh.googleusercontent.com/1Y_VGOwYBFGY30KWxT4EpFkxkhr4VXAnMdPtbF56yUVpPkbSVV5mGdCvw1RI7aNX8Q"
    )

    db.session.bulk_save_objects([user, ponto_coleta, cupom])
    db.session.commit()

    entrega_confirmada = Entrega(
        estado=2,
        usuario=1,
        ponto_coleta=1,
        descricao="Entrega no ponto de coleta da unb",
        nome_produto="Celular Samsung J5 Pro",
        categoria="Smartphone",
        pontuacao="500",
        img="https://t2.tudocdn.net/279701?w=151&h=304"
    )

    entrega_pendente = Entrega(
        estado=1,
        ponto_coleta=1,
        descricao="Entrega no ponto de coleta da unb",
        nome_produto="Bateria de carro Moura",
        categoria="Bateria",
        img="https://s34918.pcdn.co/wp-content/themes/moura_portal_pagely/assets/images/content/automotive/bateria-automotiva.png"
    )

    db.session.bulk_save_objects([entrega_confirmada, entrega_pendente])
    db.session.commit()



