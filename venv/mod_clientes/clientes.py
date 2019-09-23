#coding: utf-8
from flask import Blueprint, render_template
from mod_login.login import validaSessao

bp_clientes = Blueprint('clientes', __name__, url_prefix='/clientes', template_folder='templates')

@bp_clientes.route("/")
@validaSessao
def index():
    return render_template('clientes_index.html')
    
@bp_clientes.route("/clientes_new")
@validaSessao
def clientes():
    return render_template('clientes_new.html')