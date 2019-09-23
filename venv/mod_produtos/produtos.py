#coding: utf-8
from flask import Blueprint, render_template
from mod_login.login import validaSessao

bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='templates')

@bp_produtos.route("/")
@validaSessao
def index():
    return render_template('produtos_index.html')

@bp_produtos.route("/produtos_new")
@validaSessao
def produtos_new():
    return render_template('produtos_new.html')


    