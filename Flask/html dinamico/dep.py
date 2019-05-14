class Departamento():
    def __init__(self, nome):
        self._nome = nome
    
    def __str__(self):
        return 'Nome: {}, Codigo: {}, Gerente: {}'. format(self.obterNome(), self.obterCodigo(), self.obterGerente())


    def alterarNome(self, nome):
        self._nome = nome
    def alterarCodigo(self, codigo):
        self._codigo = codigo
    def alterarGerente(self, gerente):
        self._gerente = gerente
    
    def obterNome(self):
        return self._nome
    def obterCodigo(self):
        return self._codigo
    def obterGerente(self):
        return self._gerente if self._gerente != None else 'Nenhum registrado'

    nome = property(obterNome, alterarNome)
    codigo = property(obterCodigo, alterarCodigo)
    gerente = property(obterGerente, alterarGerente)
