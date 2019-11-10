from BancoDB import Banco

class ValidaUser(object):

    def __init__(self, id=0, username="", password="", type="",nome=""):
        self.info = {}
        self.id = id
        self.username = username
        self.password = password
        self.type = type
        self.nome = nome

    def validaUsuario(self, username, password):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [ID]  ,[Login] ,[Senha] , [Grupo],nome  FROM [dbo].[tb_Clientes] where Login = %s and Senha = %s", (username , password))
            result = c.fetchall()
            c.close()
            return result 
        except:
            return "Ocorreu um erro na busca do usuário"