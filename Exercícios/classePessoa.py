class Pessoa:
    def __init__(self, nome, dtNascimento, tel):
        self._nome = nome
        self._dtnascimento = dtNascimento
        self._telefone = tel
    
    def __str__(self):
        return "Olá, meu nome é %s\nData de nascimento: %s\nTelefone: %s" % (self._nome, self._dtnascimento, self._telefone)

    def _setNome(self, nome):
        self._nome = nome
    def _setdtNascimento(self, dtNascimento):
        self._dtnascimento = dtNascimento
    def _setTel(self, tel):
        self._telefone = tel
    
    def _getNome(self):
        return self._nome
    def _getdtNascimento(self):
        return self._dtnascimento
    def _getTel(self):
        return self._telefone

    _nome = property(_getNome, _setNome)
    _dtnascimento = property(_getdtNascimento, _setdtNascimento)
    _telefone = property(_getTel, _setTel)

obj = Pessoa(input("Informe seu nome: "), input("Informe sua data de nascimento: "), input("Informe seu telefone: "))
print(obj.__str__())
print(obj._setNome('Julio'))
print(obj.__str__())
