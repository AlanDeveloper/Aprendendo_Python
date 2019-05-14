#!-*- conding: utf8 -*-
import psycopg2
from dep import Departamento

class depDAO():
    def conectar(self):
        banco = "dbname=flask user=postgres password=postgres host=localhost port=5432"
        return psycopg2.connect(banco)

    def buscarDepartamento(self, codigo):
        conexao = self.conectar().cursor()
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
        conexao = self.conectar().cursor()
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
        conexao = self.conectar()

        conexao.cursor().execute("INSERT INTO departamento (nome) VALUES (%s)", [dep.obterNome()])
        conexao.commit()

        conexao.close()