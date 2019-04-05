class Door():
    def __init__(self, status, color, dimX, dimY):
        self._status = status
        self._color = color
        self._dimX = dimX
        self._dimY = dimY

    def openDoor(self): self._status = True
    def closeDoor(self): self._status = False
    def paintDoor(self, color): self._color = color
    def statusDoor(self): return True if self._status else False
    def __str__(self): return 'Porta: {}, Cor: {}, Dimensão: {}x{}'.format('aberta' if self.statusDoor() else 'fechada', self._color, self._dimX, self._dimY)

    def getColor(self): return self._color
    def getDimX(self): return self._dimX
    def getDimY(self): return self._dimY
    
    def setDimX(self, dimX): self._dimX = dimX
    def setDimY(self, dimY): self._dimY = dimY

    status = property(openDoor, closeDoor)
    color = property(getColor, paintDoor)
    dimX = property(getDimX, setDimX)
    dimY = property(getDimY, setDimY)

minhaPorta = Door(False, 'vermelho', 10, 5)
minhaPorta.openDoor()
minhaPorta.paintDoor('verde')
print(minhaPorta.__str__())