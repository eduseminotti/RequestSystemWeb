#coding: utf-8
from flask import Blueprint, render_template
from mod_login.login import validaSessao

bp_pedidos = Blueprint('pedidos', __name__, url_prefix='/pedidos', template_folder='templates')

@bp_pedidos.route("/")
@validaSessao
def index():
    return render_template('pedidos_index.html')

@bp_pedidos.route("/pedidos_new")
@validaSessao
def pedidos_new():
    return render_template('pedidos_new.html')
    