from BancoDB import Banco

class Produtos(object):

    def __init__(self, id=0, nome="",unidade="", quantidade="", image=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.unidade = unidade 
        self.quantidade = quantidade
        self.image = image

    def selectProdutos(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT id ,[nome],[unidade],[quantidade],image FROM [Produtos]")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do produto"

    def selectOne(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute(" SELECT id ,[nome],[unidade],[quantidade],image FROM [Produtos] where id =  %s" , (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do produto"            

    def insereProduto(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("  insert into [Produtos] (nome, unidade ,quantidade , image) VALUES  ( %s, %s, %s,%s)" 
            , (self.nome, self.unidade, self.quantidade, self.image))          
           
            banco.conexao.commit()
            c.close()

            return "produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do produto"

    def deleteProduto(self):
        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("delete from produtos where id =  %s" , (self.id))
            banco.conexao.commit()
            c.close()

            return "produto excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do produto"   

    def updateProduto(self):
        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update Produtos set nome = %s , unidade= %s , quantidade = %s , image = %s where id = %s" 
            , (self.nome ,  self.unidade , self.quantidade, self.image, self.id ))
            banco.conexao.commit()
            c.close()

            return "produto atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do produto"
    