#coding: utf-8
from flask import Flask

from mod_home.home import bp_home
from mod_login.login import bp_login
from mod_clientes.clientes import bp_clientes
from mod_pedidos.pedidos import bp_pedidos
from mod_produtos.produtos import bp_produtos
from mod_usuarios.usuarios import bp_usuarios

app = Flask(__name__)

app.register_blueprint(bp_home)
app.register_blueprint(bp_login)
app.register_blueprint(bp_clientes)
app.register_blueprint(bp_pedidos)
app.register_blueprint(bp_produtos)
app.register_blueprint(bp_usuarios)

if __name__ == '__main__':
    app.run() 