class Window:
    def __init__(self, color, glass, leaf, dimX, dimY):
        self._color = color
        self._glass = glass
        self._leaf = leaf
        self._dimX = dimX
        self._dimY = dimY
    def __str__(self): return 'Cor: {}, Vidros: {}, Folhas: {}, Dimensões: {}x{}'.format(self._color, self.getGlass(), self.getLeaf(), self._dimX, self._dimY)

    def openGlass(self): self._glass = True
    def closeGlass(self): self._glass = False

    def openLeaf(self): self._leaf = True
    def closeLeaf(self): self._leaf = False

    def openAll(self):
        self._leaf = True
        self._glass = True
    def closeAll(self):
        self._leaf = False
        self._glass = False

    def getLeaf(self): return  'Abertas' if self._leaf else 'Fechados'
    def getGlass(self): return 'Abertos' if self._glass else 'Fechadas'

    def paintWindow(self, color): self._color = color
    def area(self): return self._dimX  * self._dimY

    def setDimX(self, x): self._dimX = x
    def setDimY(self, y): self._dimY = y

janela = Window('Azul', False, False, 10, 10)
janela.openGlass()
janela.openLeaf()
print(janela.__str__())