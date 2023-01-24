from flask import render_template, request, redirect, Blueprint, url_for
from database.models import Usuario
from database.database import db, lm
from flask_login import login_user, logout_user, login_required, current_user

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['POST', 'GET'])
def cadastro():
  if request.method=='GET':
    return render_template('login.html')
  
  if request.method=='POST':
    nome = request.form.get('nome')
    matricula = request.form.get('matricula')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    usuario = Usuario(nome, matricula, email, senha, False, False)
    db.session.add(usuario)
    db.session.commit()

    return redirect('/login')

@bp_usuarios.route('/recovery')
def recovery(): 
  if not current_user.admin:
    return 'Acesso não permitido'
    return redirect('/login')
    
  usuarios = Usuario.query.all()
  return render_template('recovery.html', usuarios = usuarios)

@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  if not current_user.admin:
    return 'Acesso não permitido'
    return redirect('/login')
    
  usuario = Usuario.query.get(id)
  if id and request.method=='GET':
    return render_template('usuarios_update.html', usuario=usuario)
    
  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    matricula = request.form.get('matricula')
    senha = request.form.get('senha')
    admin = request.form.get('admin')
    professor = request.form.get('professor')
    
    usuario.nome = nome
    usuario.email = email
    usuario.matricula = matricula
    usuario.senha = senha
    usuario.admin = eval(admin)
    usuario.professor = eval(professor)

    db.session.add(usuario) 
    db.session.commit()
    return redirect(url_for('.recovery', id=id))

@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  if not current_user.admin:
    return 'Acesso não permitido'
    return redirect('/login')
    
  if id==0:
    return 'É preciso definir um usuário para ser excluído'
    return redirect(url_for('usuarios'))

  if request.method == 'GET':
    usuario = Usuario.query.get(id)
    return render_template('usuarios_delete.html', usuario = usuario)

  if request.method == 'POST':
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('.recovery'))

@lm.user_loader
def load_user(id):
  usuario = Usuario.query.filter_by(id=id).first()
  return usuario

@bp_usuarios.route('/dashboard', methods=['POST'])
def login():
  matricula = request.form.get('matricula')
  senha = request.form.get('senha')
  usuario = Usuario.query.filter_by(matricula = matricula).first()
  try:
    if (usuario.matricula == matricula and senha == usuario.senha):
      login_user(usuario)
      return render_template('dashboard.html', usuario = usuario)
    else:
      return 'senha errada'
  except:
    print('usuario não encontrado')
    return render_template('acesso_negado.html')
  finally: 
    print(usuario)

@bp_usuarios.route('/logoff')
def logoff():
  logout_user()
  return redirect('/')