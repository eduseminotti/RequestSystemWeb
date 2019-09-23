#coding: utf-8
from flask import Blueprint, render_template, request , redirect , url_for
from mod_login.login import validaSessao

bp_home = Blueprint('home', __name__, url_prefix='/home', template_folder='templates')

@bp_home.route("/")
@validaSessao
def index():
    return render_template('home_index.html')


@bp_home.route("/resultado/", methods=['GET','POST'])
@validaSessao
def resultado():
    int1 = int( request.form.get('nome'))
    int2 = int( request.form.get('idade'))
    result = int1 + int2
 
    return "Numero 1: {}<br>Numero 2: {}<br> resultado: {}".format(int1,int2, result)
        
