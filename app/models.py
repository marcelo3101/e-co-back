from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Usuario(Model):
    __tablename__="usuarios"
    email = Column(String(75), primary_key=True)
    nome =  Column(String(40), nullable=False)
    ecopoints = Column(Integer)

    def __repr__(self):
        return self.email   

class Entrega(Model):
    __tablename__="entregas"
    id_entrega = Column(String(75), primary_key=True)
    estado = Column(String(75), nullable=False)
    usuario = Column(String(75), ForeignKey('Usuario.email'),nullable=False)
    ponto_coleta = Column(String(40), ForeignKey('Ponto_Coleta.nome'), nullable=False)
    descricao =  Column(String(200))
    categoria =  Column(String(40))
    pontuacao = Column(Integer)


class PontoColeta(Model):
    __tablename__="pontos_coleta"
    nome = Column(String(40), primary_key=True)
    descricao =  Column(String(200))
    endereco =  Column(String(200), nullable=False)
   
    def __repr__(self):
        return self.nome   

class Cupom(Model):
    __tablename__="cupons"
    codigo = Column(String(20), primary_key=True)
    nome =  Column(String(40), nullable=False)
    empresa =  Column(String(50), nullable=False)
    descricao =  Column(String(200))
    custo = Column(Integer,nullable=False)
    data_validade = Column(Date,nullable=False)

    def __repr__(self):
        return self.codigo


