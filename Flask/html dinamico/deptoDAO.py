#!-*- conding: utf8 -*-
from server import serverDAO
from dep import Departamento
import psycopg2

class depDAO(serverDAO):
    def buscarDepartamento(self, codigo):
        conexao = super().conectar().cursor()
        conexao.execute('SELECT * FROM departamento')
        try:
            conexao.execute('SELECT * FROM departamento WHERE codigo = %s', [codigo])
            resposta = conexao.fetchall()

            qt = Departamento(resposta[0][0])
            qt.alterarCodigo(resposta[0][1])
            qt.alterarGerente(resposta[0][2])

            return qt
        except UnboundLocalError:
            return codigo
        except IndexError:
            return 'Codigo nao encontrado'
        conexao.close()

    def buscarDepartamentos(self):
        conexao = super().conectar().cursor()
        conexao.execute('SELECT * FROM departamento')
        resposta = conexao.fetchall()
        deptos = []

        for qt in resposta:
            obj = Departamento(qt[0])
            obj.alterarCodigo(qt[1])
            obj.alterarGerente(qt[2])
            deptos.append(obj)

        return deptos
        conexao.close()
    
    def inserirDepartamento(self, dep):
        conexao = super().conectar()

        conexao.cursor().execute("INSERT INTO departamento (nome) VALUES (%s)", [dep.obterNome()])
        conexao.commit()

        conexao.close()