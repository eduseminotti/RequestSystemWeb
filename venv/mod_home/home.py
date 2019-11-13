#coding: utf-8
from flask import Blueprint, render_template, request , redirect , url_for
from mod_login.login import validaSessao

bp_home = Blueprint('home', __name__, url_prefix='/home', template_folder='templates')

@bp_home.route("/")
@validaSessao
def index():
    return render_template('home_index.html')



        
