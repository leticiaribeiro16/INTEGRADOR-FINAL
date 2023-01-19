from flask import render_template, request, redirect, url_for
from database.models import Demanda
from database.database import db
from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required

bp_demanda = Blueprint("demanda", __name__, template_folder='templates')

@bp_demanda.route('/recovery')
def recovery():
	demanda = Demanda.query.all()
	return render_template('demanda_recovery.html', demanda = demanda)

@bp_demanda.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('demanda_create.html')

	if request.method=='POST':
		materia = request.form.get('materia')
		observacoes = request.form.get('observacoes')
		requisitos = request.form.get('requisitos')
		vagas_matutino = request.form.get('vagas_matutino')
		vagas_vespertino = request.form.get('vagas_vespertino')
		vagas_noturno = request.form.get('vagas_noturno')
		vagas_flexivel = request.form.get('vagas_flexivel')
		bolsas_matutino = request.form.get('bolsas_matutino')
		bolsas_vespertino = request.form.get('bolsas_vespertino')
		bolsas_noturno = request.form.get('bolsas_noturno')
		bolsas_flexivel = request.form.get('bolsas_flexivel')
    
		demanda = Demanda(materia, observacoes, requisitos, vagas_matutino, vagas_vespertino, vagas_noturno, vagas_flexivel, bolsas_matutino, bolsas_vespertino, bolsas_noturno, bolsas_flexivel)
		db.session.add(demanda)
		db.session.commit()

		return redirect('/demanda/recovery')

@bp_demanda.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  if id and request.method=='GET':
    demanda = Demanda.query.get(id)
    return render_template('demanda_update.html', demanda=demanda)

  if request.method=='POST':
    demanda = Demanda.query.get(id)
    demanda.materia = request.form.get('materia')
    demanda.observacoes = request.form.get('observacoes')
    demanda.requisitos = request.form.get('requisitos')
    demanda.vagas_matutino = request.form.get('vagas_matutino')
    demanda.vagas_vespertino = request.form.get('vagas_vespertino')
    demanda.vagas_noturno = request.form.get('vagas_noturno')
    demanda.vagas_flexivel = request.form.get('vagas_flexivel')
    demanda.bolsas_matutino = request.form.get('bolsas_matutino')
    demanda.bolsas_vespertino = request.form.get('bolsas_vespertino')
    demanda.bolsas_noturno = request.form.get('bolsas_noturno')
    demanda.bolsas_flexivel = request.form.get('bolsas_flexivel')

  db.session.add(demanda) 
  db.session.commit()
  return redirect(url_for('.recovery', id=id))

@bp_demanda.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  if request.method == 'GET':
    demanda = Demanda.query.get(id)
    return render_template('demanda_delete.html', demanda = demanda)

  if request.method == 'POST':
    demanda = Demanda.query.get(id)
    db.session.delete(demanda)
    db.session.commit()
    return redirect('/demanda/recovery')