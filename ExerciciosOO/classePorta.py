class Porta():
    def __init__(self, aberta, cor, dimX, dimY):
        self._aberta = aberta
        self._cor = cor
        self._dimX = dimX
        self._dimY = dimY

    def _abre(self):
        self._aberta = True
    def _feche(self):
        self._feche = False
    def _pinta(self, cor):
        self._cor = cor
    def _esta_aberta():
        return 'A porta está {}'.format(self._aberta)
    def __str__(self):
        return 'A porta está {}, cor: {}, Dimensão: {}x{}'.format(self._aberta, self._cor, self._dimX, self._dimY)

    def _getAberta(self):
        return self._aberta
    def _getCor(self):
        return self._cor
    def _getDimX(self):
        return self._dimX
    def _getDimY(self):
        return self._dimY
    
    def _setDimX(self, dimX):
        self._dimX = dimX
    def _setDimY(self, dimY):
        self._dimY = dimY

    aberta = property(_getAberta, _feche)
    cor = property(_getCor, _pinta)
    dimX = property(_getDimX, _setDimX)
    dimY = property(_getDimY, _setDimY)

minhaPorta = Porta(False, 'vermelho', 10, 5)
minhaPorta._abre()
minhaPorta._pinta('verde')
print(minhaPorta.__str__())