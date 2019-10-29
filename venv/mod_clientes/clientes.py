#coding: utf-8
from flask import Blueprint, render_template , request , redirect , url_for
from mod_login.login import validaSessao
from ClientesDB import Clientes

bp_clientes = Blueprint('clientes', __name__, url_prefix='/clientes', template_folder='templates')

@bp_clientes.route("/")
@validaSessao
def index():

    clientes = Clientes()

    result = clientes.selecALLClients()

    return render_template('clientes_index.html', result=result)
    
@bp_clientes.route("/clientes_new")
@validaSessao
def clientes_new():
    return render_template('clientes_new.html')

@bp_clientes.route("/EditClient", methods=['POST'])
@validaSessao
def EditClient():
    clientes = Clientes()

    clientes.id = request.form['id']

    res = clientes.selectClient()

    return render_template('clientes_Edit.html', result=res)

@bp_clientes.route("/UpdateClient", methods=['POST'])
@validaSessao
def UpdateClient():
    clientes = Clientes()

    clientes.id = request.form['id']
    clientes.nome = request.form['Nome']
    clientes.endereco = request.form['Endereco']
    clientes.email = request.form['Email']
    clientes.login = request.form['Login']
    clientes.senha = request.form['Senha']
    clientes.grupo = request.form['Grupo']

    exec = clientes.updateClient()

    return redirect(url_for('clientes.index', result=exec))    
    
@bp_clientes.route("/AddClient" , methods=['POST'])
@validaSessao
def AddClient():

    clientes = Clientes()

    clientes.nome = request.form['Nome']
    clientes.endereco = request.form['Endereco']
    clientes.email = request.form['Email']
    clientes.login = request.form['Login']
    clientes.senha = request.form['Senha']
    clientes.grupo = request.form['Grupo']

    exec = clientes.insertClient()
    
    return redirect(url_for('clientes.index', result=exec))    

@bp_clientes.route('/DeleteClient', methods=['POST'])
@validaSessao
def DeleteClient():

    clientes = Clientes()

    clientes.id = request.form['id']

    exec = clientes.deleteClient()

    return redirect(url_for('clientes.index', result=exec))     