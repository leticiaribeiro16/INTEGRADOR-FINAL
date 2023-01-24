from flask import render_template, request, redirect, Blueprint, url_for
from database.models import Inscricao, Usuario
from database.database import db
from flask_login import current_user

bp_inscricao = Blueprint('inscricao', __name__, template_folder='templates')

@bp_inscricao.route('/recovery')
def recovery():
  if request.method=='GET':
    inscricao = Inscricao.query.all()
    return render_template('inscricao_recovery.html', inscricao = inscricao)

@bp_inscricao.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('inscricao_create.html')

  if request.method=='POST':
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    turno = request.form.get('turno')
    matricula = request.form.get('matricula')
    telefone = request.form.get('telefone')
    inscricao = Inscricao(nome, cpf, email, turno, matricula, telefone)
    db.session.add(inscricao)
    db.session.commit()

  return redirect('/inscricao/recovery')

#RECOVERY
@bp_inscricao.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  if id and request.method=='GET':
    inscricao = Inscricao.query.get(id)
    return render_template('inscricao_update.html', inscricao=inscricao)

  if request.method=='POST':
    inscricao = Inscricao.query.get(id)
    inscricao.nome = request.form.get('nome')
    inscricao.cpf = request.form.get('cpf')
    inscricao.email = request.form.get('email')
    inscricao.turno= request.form.get('turno')
    inscricao.matricula = request.form.get('matricula')
    inscricao.telefone = request.form.get('telefone')
    
  db.session.add(inscricao) 
  db.session.commit()
  return redirect(url_for('.recovery', id=id))

#DELETE
@bp_inscricao.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  if id==0:
    return 'É preciso definir uma inscrição para ser excluída'
    return redirect(url_for('/inscricao/recovery'))

  if request.method == 'GET':
    inscricao = Inscricao.query.get(id)
    return render_template('inscricao_delete.html', inscricao = inscricao)

  if request.method == 'POST':
    inscricao = Inscricao.query.get(id)
    db.session.delete(inscricao)
    db.session.commit()
    return 'Inscrição excluída'
    return redirect(url_for('/inscricao/recovery'))
