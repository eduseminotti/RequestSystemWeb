#coding: utf-8
from flask import Flask ,request , session, redirect , url_for  
from ClientesDB import Clientes
from datetime import timedelta

from mod_home.home import bp_home
from mod_login.login import bp_login
from mod_clientes.clientes import bp_clientes
from mod_produtos.produtos import bp_produtos
from mod_Erro.erro import bp_erro

 
import os, sys
import pymssql

app = Flask(__name__)

app.register_blueprint(bp_home)
app.register_blueprint(bp_login)
app.register_blueprint(bp_clientes)
app.register_blueprint(bp_produtos)
app.register_blueprint(bp_erro)

app.secret_key = os.urandom(12).hex()

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)

if __name__ == '__main__':
    app.run() 