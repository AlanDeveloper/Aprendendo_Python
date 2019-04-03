from classePorta import Porta
from classeJanela import Janela

class Casa():
    def __init__(self, cor, lista_de_portas, lista_de_janelas):
        self._cor = cor
        self._lista_de_portas = lista_de_portas
        self._lista_de_janelas = lista_de_janelas
    def __str__(self):
        return 'Minha casa tem cor {}, janelas {} e portas {}'.format(self._cor, self.totalJanelas(), self.totalPortas())

    def pinta(self, cor):
        self._cor = cor
    def inserePorta(self, porta):
        self._lista_de_portas.append(porta)
    def insereJanela(self, janela):
        self._lista_de_janelas.append(janela)

    def removePorta(self, pos):
        self._lista_de_portas.remove(pos)
    def removeJanela(self, pos):
        self._lista_de_janelas.remove(pos)

    def corDaCasa(self):
        return self._cor()
    def janelasDaCasa(self):
        return self._lista_de_janelas
    def portasDaCasa(self):
        return self._lista_de_portas

    def portasAbertas(self):
        cont = 0
        for i in range(0, len(self._lista_de_portas)):
            if(self._lista_de_portas[i]._esta_aberta() == True): cont += 1
        return cont
    def janelasAbertas(self):
        cont = 0
        for i in range(0, len(self._lista_de_janelas)):
            if(self._lista_de_janelas[i]._esta_aberta() == True): cont += 1
        return cont

    def totalPortas(self):
        return len(self._lista_de_portas)
    def totalJanelas(self):
        return len(self._lista_de_janelas)

minhaCasa = Casa('Vermelho', [], [])
minhaCasa.pinta('Verde')
print(minhaCasa.__str__())

porta1 = Porta(False, 'Verde', 10, 5)
janela1 = Janela('Azul', False, False, 10, 10)
minhaCasa.insereJanela(janela1)
minhaCasa.inserePorta(porta1)
print(minhaCasa.__str__())

print(minhaCasa.janelasDaCasa()[0].__str__())
print(minhaCasa.portasDaCasa()[0].__str__())

print('Total de portas: {}, Total de Janelas: {}'.format(minhaCasa.totalPortas(), minhaCasa.totalJanelas()))