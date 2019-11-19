#coding: utf-8
from base64 import b64encode

from flask import Blueprint, render_template, request, redirect, url_for, session, make_response, flash
from mod_login.login import validaSessao
from PedidosDb import Pedidos
from ProdutosDB import Produtos

import pdfkit

bp_pedidos = Blueprint('pedidos', __name__,
                       url_prefix='/pedidos', template_folder='templates')


@bp_pedidos.route("/")
@validaSessao
def index():

    pedidos = Pedidos()

    result = pedidos.selecALLPedidos()

    return render_template('pedidos_index.html', result=result)


@bp_pedidos.route("/NovoPedido")
@validaSessao
def NovoPedido():
    return pedidosEdit(0)


@bp_pedidos.route("/editPedido", methods=['POST'])
@validaSessao
def editPedido():
    pedidos = Pedidos()

    pedidos.id = request.form['id']

    return pedidosEdit(pedidos.id)


def pedidosEdit(id):

    pedidos = Pedidos()

    if id == 0:
        pedidos.Cliente = session['id']
        pedidos.id = pedidos.addpedido()
    else:
        pedidos.id = id

    cliente = pedidos.selectclientePedido()
    proddisponiveis = pedidos.selectProdutosForPedido(pedidos.id)
    prodpedidos= pedidos.selectProdutosDoPedido(pedidos.id)

    return render_template('pedidos_edit.html', prodDisponiveis=proddisponiveis, cliente=cliente, IdPedido=pedidos.id,
                           prodPedidos=prodpedidos)


@bp_pedidos.route('/DeletePedido', methods=['POST'])
@validaSessao
def DeletePedido():

    pedidos = Pedidos()

    pedidos.id = request.form['id']

    pedidos.deletepedido()

    return redirect(url_for('pedidos.index'))



@bp_pedidos.route('/incluiProduto', methods=['POST'])
@validaSessao
def incluiProduto():

    pedidos = Pedidos()
    produtos = Produtos()

    pedidos.id = request.form['IdPedido']
    pedidos.produtoId = request.form['idProduto']
    pedidos.quantidade = request.form['quantidade']

    pedidos.IncluiProdutoPedido()
    produtos.diminuiitensestoque(pedidos.produtoId, pedidos.quantidade)

    return pedidosEdit(pedidos.id)


@bp_pedidos.route('/removeproduto', methods=['POST'])
@validaSessao
def removeproduto():

    pedidos = Pedidos()
    produtos = Produtos()

    pedidos.id = request.form['IdPedido']
    pedidos.produtoId = request.form['idProduto']
    pedidos.quantidade = request.form['quantidade']

    pedidos.deletaProdutoPedido()
    produtos.aumentaitensestoque(pedidos.produtoId, pedidos.quantidade)

    return pedidosEdit(pedidos.id)

@bp_pedidos.route('/Verpedido', methods=['POST'])
def Verpedido():

    pedidos = Pedidos()

    pedidos.id = request.form['id']

    cliente = pedidos.selectclientePedido()
    prodpedidos = pedidos.selectProdutosDoPedido(pedidos.id)

    

    ren = render_template('pedidos_view.html', cliente=cliente, IdPedido=pedidos.id, prodPedidos=prodpedidos)
    pdf = pdfkit.from_string(ren, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachement; filename=relatorio-pedido.pdf'
    return response


    #return render_template('pedidos_view.html', cliente=cliente, IdPedido=pedidos.id, prodPedidos=prodpedidos)



@bp_pedidos.route('/pdfpedido')
def pdfpedido():

    return None


