import psycopg2
from departamento import Departamento
from funcionario import Funcionario

class serverDAO():
    def conectar(self):
        banco = "dbname=DOIDAO user=postgres password=postgres host=localhost port=5432"
        
        return psycopg2.connect(banco)

    def buscarDepartamento(self, codigo):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            cur.execute("SELECT * FROM departamento WHERE codigo = %s", [codigo])
            resposta = cur.fetchall()

            qt = Departamento(resposta[0][0])
            qt.alterarCodigo(resposta[0][1])
            qt.alterarGerente(self.buscarFuncionario(resposta[0][2]))

            cur.close()
            conexao.close()
            
            return qt
        except IndexError:
            return 'Coloca o código direito'
    def buscarFuncionario(self, codigo):
        conexao = self.conectar()
        cur = conexao.cursor()
        
        try:
            cur.execute("SELECT * FROM funcionario WHERE codigo = %s", [codigo])
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

    def inserirDepartamento(self, dep):
        conexao = self.conectar()
        cur = conexao.cursor()

        cur.execute("INSERT INTO departamento(nome) VALUES(%s)", [dep.obterNome()])
        conexao.commit()
        
        cur.close()
        conexao.close()
    def inserirFuncionario(self, func):
        conexao = self.conectar()
        cur = conexao.cursor()

        cur.execute("INSERT INTO funcionario (nome, coddepartamento) VALUES (%s, %s)", [func.obterNome(), func.obterDepartamento()])
        conexao.commit()
        
        cur.close()
        conexao.close()
    def alterarDepartamento(self, dep):
        conexao = self.conectar()
        cur = conexao.cursor()
        cur.execute("UPDATE departamento SET nome = %s, codgerente = %s WHERE codigo = %s", [dep.obterNome(), dep.obterGerente().obterCodigo(), dep.obterCodigo()])
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
