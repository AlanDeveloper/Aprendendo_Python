from departamento import Departamento
from funcionario import Funcionario
from serverDAO import serverDAO

departamento = Departamento('Microsoft') # Gerado automaticamente o código
funcionario = Funcionario('Fabrício', 1)

test = serverDAO()
# test.inserirDepartamento(departamento)
# test.inserirFuncionario(funcionario)

departamento = test.buscarDepartamento(1)
departamento.alterarNome('Google')
test.alterarDepartamento(departamento)

funcionario = test.buscarFuncionario(1)
funcionario.alterarNome('Julia')
test.alterarFuncionario(funcionario)

departamento.alterarGerente(test.buscarFuncionario(1))
test.alterarDepartamento(departamento)

print(test.buscarDepartamento(1).obterGerente().obterNome())