#!-*- conding: utf8 -*-
from server import serverDAO 

class funcDAO():
    def login(self, login, pas):
        conexao = serverDAO().conectar().cursor()
        try:
            conexao.execute('SELECT * FROM funcionario WHERE login = %s and pass = %s', [login, pas])
            resposta = conexao.fetchall()

            if resposta[0][0] != None:
                return True
        except UnboundLocalError:
            return False
        except IndexError:
            return False
        conexao.close()