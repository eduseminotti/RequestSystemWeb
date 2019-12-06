from BancoDB import Banco


class Pedidos(object):

    def __init__(self, id=0, Cliente="", quantidade=0,produtoId=0):
        self.info = {}
        self.id = id
        self.produtoId = produtoId
        self.Cliente = Cliente
        self.quantidade = quantidade

    def selecALLPedidoscliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT Id ,cliente = (select nome from tb_clientes where id = pedido.clientId)," +
                      "quantidade = (select COUNT(*) from ItensPedido where pedidosId = pedido.id) ,descricao,"+
                      "cast (insertdate as date)  FROM [Pedidos] as pedido where pedido.clientId = %s", (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca dos pedidos"


    def selecALLPedidosadmin(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT Id ,cliente = (select nome from tb_clientes where id = pedido.clientId)," +
                      "quantidade = (select COUNT(*) from ItensPedido where pedidosId = pedido.id) ,descricao,"+
                      "cast (insertdate as date)  FROM [Pedidos] as pedido ")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca dos pedidos"

    def addpedido(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into [Pedidos] (clientId) VALUES (%s)", (self.Cliente))

            c.execute("select max(id) from pedidos")
            result = c.fetchall()
            banco.conexao.commit()
            c.close()

            for row in result:
                result = row[0]

            return result
        except:
            return "ERRO"

    def selectclientePedido(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select cliente = (select nome from tb_clientes where id = Pedidos.clientId) "+
                      "from pedidos where id = %s", (self.id))

            result = c.fetchall()
            banco.conexao.commit()

            for row in result:
                self.Cliente = row[0]

            c.close()

            return self.Cliente
        except:
            return "ERRO"

    def deletepedido(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("delete from [dbo].[ItensPedido] where pedidosId =  %s", (self.id))

            c.execute("delete from [dbo].[pedidos] where id =  %s", (self.id))
            banco.conexao.commit()
            c.close()

            return "pedido excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do pedido"


    def selectProdutosForPedido(self,pedidoId):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT id ,[nome],[unidade],[quantidade],image FROM [Produtos] "+
                      "where id not in (select Produtosid from ItensPedido where pedidosId = %s)", pedidoId)
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"

    def selectProdutosDoPedido(self,pedidoId):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select prod.id,prod.image,prod.nome , prod.unidade, itens.quantidade from dbo.produtos as prod inner join  dbo.ItensPedido as itens  on itens.produtosId = prod.id where itens.pedidosId = %s", pedidoId)
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"

    def IncluiProdutoPedido(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("insert into ItensPedido ( pedidosId , produtosId,quantidade) "+
                      "VALUES (%s, %s,%s)", (self.id, self.produtoId, self.quantidade))
            banco.conexao.commit()
            c.close()

            return "produto incluido com sucesso no Pedido!"
        except:
            return "ERRO"

    def deletaProdutoPedido(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            c.execute("delete from ItensPedido where pedidosId = %s and produtosId = %s", (self.id, self.produtoId))
            banco.conexao.commit()
            c.close()

            return "produto removido do Pedido com sucesso !"
        except:
            return "ERRO"