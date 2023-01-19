from flask import render_template, request, redirect, Blueprint
from database.models import Usuario
from database.database import db, lm
from flask_login import login_user, current_user, logout_user, login_required

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['POST', 'GET'])
def cadastro():
  if request.method=='GET':
    return render_template('login.html')
  
  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    matricula = request.form.get('matricula')
    
    usuario = Usuario(nome, email, matricula, senha, False)
    db.session.add(usuario)
    db.session.commit()

    return redirect('/login')

@bp_usuarios.route('/recovery')
def recovery():
	usuarios = Usuario.query.all()
	return render_template('recovery.html', usuarios = usuarios)

@lm.user_loader
def load_user(id):
  usuario = Usuario.query.filter_by(id=id).all()
  return usuario

@bp_usuarios.route('/login', methods=['POST'])
def login():
  matricula = request.form.get('matricula')
  senha = request.form.get('senha')
  u = Usuario.query.filter(Usuario.matricula == matricula).first()
  print(u)
  if (u.matricula == matricula and senha == u.senha):
    login_user(u)
    return render_template('dashboard.html', usuario=u)
  else:
    return 'senha errada'

@bp_usuarios.route('/logoff')
def logoff():
  logout_user()
  return redirect('/')