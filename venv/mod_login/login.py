#coding: utf-8
from flask import Blueprint, render_template

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/")
def index():
    return render_template('Login.html')
    
