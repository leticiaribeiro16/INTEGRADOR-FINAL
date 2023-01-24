from database.database import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
  __tablename__= "usuario"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  nome = db.Column(db.String(100))
  matricula = db.Column(db.String(100))
  email = db.Column(db.String(100))
  senha = db.Column(db.String(100))
  admin = db.Column(db.Boolean)
  professor = db.Column(db.Boolean)

  def __init__(self, nome, matricula, email, senha, admin, professor):
    self.nome = nome
    self.matricula = matricula
    self.email = email
    self.senha = senha
    self.admin = admin
    self.professor = professor
  
  def __repr__(self):
      return "<Usuario {}>".format(self.nome)

class Demanda(db.Model):
  __tablename__= "demanda"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  observacoes = db.Column(db.Text)
  materia = db.Column(db.String(100))
  requisitos = db.Column(db.Text)
  vagas_matutino = db.Column(db.Float)
  vagas_vespertino = db.Column(db.Float)
  vagas_noturno = db.Column(db.Float)
  vagas_flexivel = db.Column(db.Float)
  bolsas_matutino = db.Column(db.Float)
  bolsas_vespertino = db.Column(db.Float)
  bolsas_noturno = db.Column(db.Float)
  bolsas_flexivel = db.Column(db.Float)

  def __init__(self, observacoes, materia, requisitos, vagas_matutino, vagas_vespertino, vagas_noturno, vagas_flexivel, bolsas_matutino, bolsas_vespertino, bolsas_noturno, bolsas_flexivel):
    self.observacoes = observacoes
    self.materia = materia
    self.requisitos = requisitos
    self.vagas_matutino = vagas_matutino
    self.vagas_vespertino = vagas_vespertino
    self.vagas_noturno = vagas_noturno
    self.vagas_flexivel = vagas_flexivel
    self.bolsas_matutino = bolsas_matutino
    self.bolsas_vespertino = bolsas_vespertino
    self.bolsas_noturno = bolsas_noturno
    self.bolsas_flexivel = bolsas_flexivel

    def __repr__(self):
      return "<Demanda {}>".format(self.materia)

class Inscricao(db.Model):
  __tablename__= "inscricao"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  nome = db.Column(db.String(100))
  cpf = db.Column(db.String(100))
  email = db.Column(db.String(100))
  turno = db.Column(db.String(100))
  matricula = db.Column(db.String(100))
  telefone = db.Column(db.Float)

  def __init__(self, nome, cpf, email, turno, matricula, telefone):
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.turno = turno
    self.matricula = matricula
    self.telefone = telefone
  
  def __repr__(self):
      return "<Inscricao {}>".format(self.nome)