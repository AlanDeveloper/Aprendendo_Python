import psycopg2

class serverDAO():
    def conectar(self):
        banco = "dbname=doidao user=postgres password=postgres host=localhost port=5432"
        
        return psycopg2.connect(banco)

    def inserir(self):
        conexao = self.conectar()
        cur = conexao.cursor()

        sql = 'INSERT INTO "departamento" (nome, codgerente) VALUES ({}, {})'.format("'Google'", 1)
        cur.execute(sql)
        conexao.commit()
        
        cur.close()
        conexao.close()