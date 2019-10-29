from BancoDB import Banco

class Clientes(object):

    def __init__(self, id=0, nome="",endereco="",email="", login="", senha="", grupo=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.endereco = endereco 
        self.email = email
        self.login = login
        self.senha = senha
        self.grupo = grupo


    def selecALLClients(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT  ID,nome,endereco,email,login,senha,grupo FROM dbo.tb_clientes")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca dos Clientes"

    def selectClient(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT id,[nome],[endereco],[email],[login],[senha],[grupo]FROM [dbo].[tb_clientes] where id =  %s" , (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Cliente"            

    def insertClient(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT into dbo.tb_clientes ( nome,endereco,email,login,senha,grupo ) VALUES (%s , %s ,%s , %s , %s , %s)" , (self.nome, self.endereco, self.email, self.login , self.senha, self.grupo ))          
           
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Cliente"

    def deleteClient(self):
        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("delete from [dbo].[tb_Clientes] where id =  %s" , (self.id))
            banco.conexao.commit()
            c.close()

            return "Cliente excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do Cliente"   

    def updateClient(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update [dbo].[tb_clientes]  set [nome] = %s , [endereco]  = %s , [email] = %s, [login] = %s  , [senha] = %s , [grupo] = %s where ID = %s", ( self.nome ,   self.endereco , self.email,  self.login ,  self.senha ,self.grupo, self.id))
            banco.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Cliente"
    