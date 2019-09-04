#coding: utf-8
from flask import Blueprint, render_template

bp_clientes = Blueprint('clientes', __name__, url_prefix='/clientes', template_folder='templates')

@bp_clientes.route("/")
def index():
    return render_template('clientes_index.html')
    