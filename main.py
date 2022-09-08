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

    ponto_coleta1 = PontoColeta(
        nome="Ponto de coleta Rodoviária",
        descricao="Ponto de coleta de lixo eletrônico",
        endereco="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route=-15.75917%2C-47.87075%3B-15.79385%2C-47.88337#map=15/-15.7756/-47.8608",
        latitude="-15.79384",
        longitude="-47.88338"
    )

    ponto_coleta2 = PontoColeta(
        nome="Ponto de coleta UnB",
        descricao="Ponto de coleta de lixo eletrônico",
        endereco="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route=-15.75917%2C-47.87075%3B-15.76106%2C-47.86796#map=18/-15.76017/-47.86887",
        latitude="-15.76114",
        longitude="-47.86752"
    )

    cupom1 = Cupom(
        nome="Frete grátis para qualquer pedido",
        empresa="Ifood",
        descricao="Faça seu pedido com entrega grátis para qualquer restaurante cadastrado!",
        custo=300,
        data_validade=datetime(2022, 12, 1),
        img="https://play-lh.googleusercontent.com/1Y_VGOwYBFGY30KWxT4EpFkxkhr4VXAnMdPtbF56yUVpPkbSVV5mGdCvw1RI7aNX8Q"
    )
    cupom2 = Cupom(
        nome="Sobremesa grátis",
        empresa="McDonalds",
        descricao="Receba uma sobremesa de até 15 reais gratuitamente em uma das lojas cadastradas",
        custo=400,
        data_validade=datetime(2022, 11, 1),
        img="https://www.mcdonalds.com.br/images/layout/mcdonalds-logo-bg-red.png"
    )

    db.session.bulk_save_objects([user, ponto_coleta1, ponto_coleta2, cupom1, cupom2])
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



