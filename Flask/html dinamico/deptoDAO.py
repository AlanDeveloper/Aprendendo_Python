#!-*- conding: utf8 -*-
import psycopg2
from dep import Departamento

class depDAO():
    def conectar(self):
        banco = "dbname=flask user=postgres password=postgres host=localhost port=5432"
        
        return psycopg2.connect(banco)


    def buscarDepartamentos(self):
        conexao = self.conectar()
        cur = conexao.cursor()
        cur.execute('SELECT * FROM departamento')
        resposta = cur.fetchall()
        deptos = []

        for qt in resposta:
            obj = Departamento(qt[0])
            obj.alterarCodigo(qt[1])
            deptos.append(obj)
            

        return deptos
        cur.close()
        conexao.close()