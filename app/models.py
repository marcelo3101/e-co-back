from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app import db

class Usuario(db.Model):
    __tablename__="usuarios"
    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), unique=True, index=True)
    email = Column(String(75), unique=True)
    nome =  Column(String(40), nullable=False)
    ecopoints = Column(Integer)

    def __repr__(self):
        return self.email   

class Entrega(db.Model):
    __tablename__="entregas"
    id = Column(Integer, primary_key=True)
    estado = Column(Integer, nullable=False) # 1 - pendente, 2 - confirmada
    usuario = Column(Integer, ForeignKey("usuarios.id"),nullable=True)
    ponto_coleta = Column(Integer, ForeignKey("pontos_coleta.id"), nullable=False)
    descricao =  Column(String(200), nullable=True)
    nome_produto =  Column(String(40), nullable=False)
    categoria =  Column(String(40), nullable=False)
    pontuacao = Column(Integer, nullable=True)
    img = Column(String(300), nullable=True)


class PontoColeta(db.Model):
    __tablename__="pontos_coleta"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), unique=True)
    descricao =  Column(String(200))
    latitude = Column(String(80))
    longitude = Column(String(80))
    endereco =  Column(String(300), nullable=False)
   
    def __repr__(self):
        return self.nome   

class Cupom(db.Model):
    __tablename__="cupons"
    id = Column(Integer, primary_key=True)
    nome =  Column(String(40), nullable=False)
    empresa =  Column(String(50), nullable=False)
    descricao =  Column(String(200))
    custo = Column(Integer,nullable=False)
    data_validade = Column(db.DateTime,nullable=False)
    img = Column(String(300), nullable=True)

    def __repr__(self):
        return self.id

class CupomResgatado(db.Model):
    __tablename__="cupons_resgatados"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cupom_id = Column(Integer, ForeignKey("cupons.id"), nullable=False)    
