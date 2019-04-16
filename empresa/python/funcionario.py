class funcionario():
    def __init__(self, nome, departamento):
        self._nome = nome
        self._departamento = departamento
        self._codigo

    def alterarNome(self, nome):
        self._nome = nome
    def alterarCodigo(self, codigo):
        self._codigo = codigo
    def alterarDepartamento(self, departamento):
        self._departamento = departamento

    def obterNome(self):
        return self._nome
    def obterCodigo(self):
        return self._codigo
    def obterDepartamento(self):
        return self._departamento

    nome = property(obterNome, alterarNome)
    codigo = property(obterCodigo, alterarCodigo)
    departamento = property(obterDepartamento, alterarDepartamento)