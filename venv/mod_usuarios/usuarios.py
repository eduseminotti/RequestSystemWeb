#coding: utf-8
from flask import Blueprint, render_template
from mod_login.login import validaSessao

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')

@bp_usuarios.route("/")
@validaSessao
def index():
    return render_template('usuarios_index.html')

@bp_usuarios.route("/usuarios_new")
@validaSessao
def usuarios_new():
    return render_template('usuarios_new.html')
    