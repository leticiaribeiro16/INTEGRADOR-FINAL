from flask import Flask, render_template
from flask import redirect
from flask_login import current_user
from database.database import db, lm
from flask_migrate import Migrate
from database.models import Usuario
from database.models import Demanda
from controllers.usuarios import bp_usuarios
from controllers.demanda import bp_demanda

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HELP'
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_demanda, url_prefix='/demanda')

conexao = "sqlite:///meubanco.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
	if current_user.is_authenticated:
		return render_template('dashboard.html')
	else:
		return redirect('/login')
  
@app.route('/login')
def login():
    return render_template('login.html')

# @app.errorhandler(401)
# def acesso_negado(e):
#     return render_template('acesso_negado.html'), 404

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
