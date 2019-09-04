#coding: utf-8
from flask import Blueprint, render_template

bp_pedidos = Blueprint('pedidos', __name__, url_prefix='/pedidos', template_folder='templates')

@bp_pedidos.route("/")
def index():
    return render_template('pedidos_index.html')
    