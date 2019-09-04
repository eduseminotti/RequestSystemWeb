#coding: utf-8
from flask import Blueprint, render_template

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')

@bp_usuarios.route("/")
def index():
    return render_template('usuarios_index.html')
    