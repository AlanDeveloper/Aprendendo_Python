import psycopg2
from func import Funcionario

class serverDAO():
    def conectar(self):
        banco = "dbname=DOIDAO user=postgres password=postgres host=localhost port=5432"
        
        return psycopg2.connect(banco)


    def buscarFuncionario(self, codigo):
        conexao = self.conectar()
        cur = conexao.cursor()

        try:
            cur.execute(
                "SELECT * FROM funcionario WHERE codigo = %s", [codigo])
            resposta = cur.fetchall()

            qt = Funcionario(resposta[0][0], resposta[0][2])
            qt.alterarCodigo(resposta[0][1])

            return qt
        except UnboundLocalError:
            return codigo
        except IndexError:
            return 'Coloca o código direito'

        cur.close()
        conexao.close()


    def inserirFuncionario(self, func):
        conexao = self.conectar()
        cur = conexao.cursor()

        cur.execute("INSERT INTO funcionario (nome, coddepartamento) VALUES (%s, %s)", [
                    func.obterNome(), func.obterDepartamento()])
        conexao.commit()

        cur.close()
        conexao.close()


    def alterarFuncionario(self, func):
        conexao = self.conectar()
        cur = conexao.cursor()

        cur.execute("UPDATE funcionario SET nome = %s, coddepartamento = %s WHERE codigo = %s", [
                    func.obterNome(), func.obterDepartamento(), func.obterCodigo()])
        conexao.commit()

        cur.close()
        conexao.close()
