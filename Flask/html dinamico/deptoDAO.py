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

<<<<<<< HEAD
            qt = Departamento(resposta[0][0])
            qt.alterarCodigo(resposta[0][1])
            qt.alterarGerente(resposta[0][2])

=======
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

>>>>>>> 6d9e546586af24cf73778705315e89eb9c53f1f7
            return qt
        except UnboundLocalError:
            return codigo
        except IndexError:
            return 'Codigo nao encontrado'
        conexao.close()

    def buscarDepartamentos(self):
<<<<<<< HEAD
        conexao = super().conectar().cursor()
=======
        conexao = self.conectar().cursor()
>>>>>>> 6d9e546586af24cf73778705315e89eb9c53f1f7
        conexao.execute('SELECT * FROM departamento')
        resposta = conexao.fetchall()
        deptos = []

        for qt in resposta:
            obj = Departamento(qt[0])
            obj.alterarCodigo(qt[1])
            obj.alterarGerente(qt[2])
<<<<<<< HEAD
            deptos.append(obj)
=======
            deptos.append(obj) 
>>>>>>> 6d9e546586af24cf73778705315e89eb9c53f1f7

        return deptos
        conexao.close()
    
    def inserirDepartamento(self, dep):
<<<<<<< HEAD
        conexao = super().conectar()
=======
        conexao = self.conectar()
>>>>>>> 6d9e546586af24cf73778705315e89eb9c53f1f7

        conexao.cursor().execute("INSERT INTO departamento (nome) VALUES (%s)", [dep.obterNome()])
        conexao.commit()

        conexao.close()