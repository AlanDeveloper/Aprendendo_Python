from departamento import Departamento
from funcionario import Funcionario
from serverDAO import serverDAO

departamento = Departamento('Google')

funcionario = Funcionario('Fabrício')


test = serverDAO()
test.inserir()