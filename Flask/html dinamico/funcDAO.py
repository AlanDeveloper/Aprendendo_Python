#!-*- conding: utf8 -*-
import psycopg2
from func import Funcionario

class funcDAO():
    def conectar(self):
        banco = "dbname=flask user=postgres password=postgres host=localhost port=5432"
        return psycopg2.connect(banco)

    def buscarFuncionario(self, codigo):
        conexao = self.conectar().cursor()
        try:
            conexao.execute('SELECT * FROM funcionario WHERE codigo = %s', [codigo])
            resposta = conexao.fetchall()

            qt = Funcionario(resposta[0][0], resposta[0][2])
            qt.alterarCodigo(resposta[0][1])

            return qt
        except UnboundLocalError:
            return codigo
        except IndexError:
            return 'Codigo nao encontrado'
        conexao.close()

    def buscarFuncionarios(self):
        conexao = self.conectar().cursor()
        conexao.execute('SELECT * FROM funcionario')
        resposta = conexao.fetchall()
        funcs = []

        for qt in resposta:
            obj = Funcionario(qt[0], qt[2])
            obj.alterarCodigo(qt[1])
            funcs.append(obj)

        return funcs
        conexao.close()

    def inserirFuncionario(self, func):
        conexao = self.conectar()

        conexao.cursor().execute("INSERT INTO funcionario (nome, coddepartamento) VALUES (%s, %s)", [func.obterNome(), func.obterDepartamento()])
        conexao.commit()

        conexao.close()

    def alterarFuncionario(self, func):
        conexao = self.conectar()
        cur = conexao.cursor()

        cur.execute("UPDATE funcionario SET nome = %s, coddepartamento = %s WHERE codigo = %s", [
                    func.obterNome(), func.obterDepartamento(), func.obterCodigo()])
        conexao.commit()

        cur.close()
        conexao.close()