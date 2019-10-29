#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from mod_login.login import validaSessao
from ProdutosDB import Produtos

import base64

bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='templates')

@bp_produtos.route("/")
@validaSessao
def index():
    produtos = Produtos()

    produtos = produtos.selectProdutos()
    
    return render_template('produtos_index.html', produtos=produtos)

@bp_produtos.route("/produtos_new")
@validaSessao
def produtos_new():


    return render_template('produtos_new.html')

@bp_produtos.route("/AddProduto",methods=['POST'])
@validaSessao
def AddProduto():
    produtos = Produtos()

    produtos.nome = request.form['nome']
    produtos.unidade = request.form['unidade']
    produtos.quantidade = request.form['quantidade']

    
    produtos.image =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")

    produtos.insereProduto()    

    return redirect(url_for('produtos.index'))   


@bp_produtos.route("/EditaProduto",methods=['POST'])
@validaSessao
def EditaProduto():

    produtos = Produtos()
    
    produtos.id = request.form['id']

    prod = produtos.selectOne()

    return render_template('EditaProduto.html', produtos=prod)


@bp_produtos.route("/UpdateProduto",methods=['POST'])
@validaSessao
def UpdateProduto():
    produtos = Produtos()
    
    produtos.id = request.form['id']
    produtos.nome = request.form['nome']
    produtos.unidade = request.form['unidade']
    produtos.quantidade = request.form['quantidade'] 

    produtos.image =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")

    exec = produtos.updateProduto()    

    return redirect(url_for('produtos.index', exe=exec))       

@bp_produtos.route("/ExcluiProduto",methods=['POST'])
@validaSessao
def ExcluiProduto():
    produtos = Produtos()

    produtos.id = request.form['id']

    produtos.deleteProduto()    

    return redirect(url_for('produtos.index'))  


    