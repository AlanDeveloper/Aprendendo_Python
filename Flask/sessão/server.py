#!-*- conding: utf8 -*-
import psycopg2

class serverDAO:
    def conectar(self):
        banco = "dbname=doidao user=postgres password=postgres host=localhost port=5432"
        return psycopg2.connect(banco)