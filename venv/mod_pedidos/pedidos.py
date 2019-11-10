#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, session
from mod_login.login import validaSessao
from PedidosDb import Pedidos
from ProdutosDB import Produtos

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

    proddisponiveis = pedidos.selectProdutosForPedido(pedidos.id)
    prodpedidos= pedidos.selectProdutosDoPedido(pedidos.id)

    return render_template('pedidos_edit.html', prodDisponiveis=proddisponiveis, IdPedido=pedidos.id,
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

    pedidos.id = request.form['IdPedido']
    pedidos.produtoId = request.form['idProduto']
    pedidos.quantidade = request.form['quantidade']

    pedidos.IncluiProdutoPedido()

    return pedidosEdit(pedidos.id)


@bp_pedidos.route('/removeproduto', methods=['POST'])
@validaSessao
def removeproduto():

    pedidos = Pedidos()

    pedidos.id = request.form['IdPedido']
    pedidos.produtoId = request.form['idProduto']

    pedidos.deletaProdutoPedido()

    return pedidosEdit(pedidos.id)
