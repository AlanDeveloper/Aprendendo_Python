from math import sqrt
class Ponto:
    def __init__(self, x, y):
        self._x =  x
        self._y =  y
    
    def _setX(self, x):
        self._x = x
    def _setY(self, y):
        self._y = y

    def _getX(self):
        print('ola')
        return self._x
    def _getY(self):
        return self._y

    def _distanciaOrigem(self):
        distanciaX = (0 - self._x) * (0 - self._x)
        distanciaY = (0 - self._y) * (0 - self._y)
        return  sqrt(distanciaX + distanciaY)
    def _distanciaEntrePontos(self, ponto):
        distanciaX = (ponto._getX() - self._x) * (ponto._getX() - self._x)
        distanciaY = (ponto._getY() - self._y) * (ponto._getY() - self._y)
        return  sqrt(distanciaX + distanciaY)
    
    _x = property(_getX, _setX)
    _y = property(_getY, _setY)

ponto1 = Ponto(int(input('Coordenada x: ')), int(input('Coordenada y: ')))
ponto2 = Ponto(int(input('Coordenada x: ')), int(input('Coordenada y: ')))
print('Distância da oridem: {}\nDistância entre pontos: {}'.format(ponto1._distanciaOrigem(), ponto1._distanciaEntrePontos(ponto2)))
ponto1._x = 3
print(ponto1._getX())
