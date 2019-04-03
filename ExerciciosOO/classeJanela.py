class Janela:
    def __init__(self, cor, vidro, folhas, dimX, dimY):
        self._cor = cor
        self._vidro = vidro
        self._folhas = folhas
        self._dimX = dimX
        self._dimY = dimY
    def __str__(self):
        return 'Cor: {}, Vidros: {}, Folhas: {}, Dimensões: {}x{}'.format(self._cor, self._vidro, self._folhas, self._dimX, self._dimY)

    def abre_vidro(self):
        self.vidro = True
    def fecha_vidro(self):
        self._vidro = False
    def abre_folhas(self):
        self._folhas = True
    def fecha_folhas(self):
        self._folhas = False
    def aberta(self):
        self._folhas = True
        self._vidro = True
    def fechada(self):
        self._folhas = False
        self._vidro = False

    def folhas_abertas(self):
        return self._folhas
    def vidro_abertas(self):
        return self._vidro
    def pinta(self, cor):
        self._cor = cor
    def area(self):
        return self._dimX  * self._dimY

    def _setDimX(self, x):
        self._dimX = x
    def _setDimY(self, y):
        self._dimY = y

janela = Janela('Azul', False, False, 10, 10)
janela.abre_vidro()
janela.abre_folhas()
print(janela.__str__())