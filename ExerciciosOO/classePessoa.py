class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        self._peso = peso
    
    def faz_aniversario(self): 
        self._idade += 1
    def _emagrece(self, peso):
        self._peso -= peso
    def _engorda(self, peso):
        self._peso += peso
    def _cresce(self, qt):
        self._altura += qt
    def __str__(self):
        return 'Nome: {}, Idade: {}, Altura: {}, Peso: {}'.format(self._nome, self._idade, self._altura, self._peso)

    def _getNome(self):
        return self._nome
    def _getIdade(self):
        return self._idade
    def _getAltura(self):
        return self._altura
    def _getPeso(self):
        return self._peso

    def _setNome(self, nome):
        self._nome = nome
    def _setIdade(self, idade):
        self._idade = idade
    def _setAltura(self, altura):
        self._altura = altura
    def _setPeso(self, peso):
        self._peso = peso

    nome = property(_getNome, _setNome)
    idade = property(_getIdade, _setIdade)
    altura = property(_getAltura, _setAltura)
    peso = property(_getPeso, _setPeso)


p1 = Pessoa('Maurício', 18, 162, 59)
p2 = Pessoa('Alan', 18, 183, 70)

p1.faz_aniversario()
p2._engorda(10)
p1._emagrece(5)
p1._cresce(2)

print(p1.__str__(), p2.__str__())