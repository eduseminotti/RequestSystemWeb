#coding: utf-8
from flask import Blueprint, render_template

bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='templates')

@bp_produtos.route("/")
def index():
    return render_template('produtos_index.html')
    