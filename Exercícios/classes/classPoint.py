from math import sqrt
class Point:
    def __init__(self, x, y):
        self._x =  x
        self._y =  y
    
    def getX(self): return self._x
    def getY(self): return self._y

    def setX(self, x): self._x = x
    def setY(self, y): self._y = y

    def distanceOrigin(self):
        distanceX = (0 - self._x) * (0 - self._x)
        distanceY = (0 - self._y) * (0 - self._y)
        return  sqrt(distanceX + distanceY)
    def distancePoints(self, point):
        distanceX = (point.getX() - self._x) * (point.getX() - self._x)
        distanceY = (point.getY() - self._y) * (point.getY() - self._y)
        return  sqrt(distanceX + distanceY)
    
    x = property(getX, setX)
    y = property(getY, setY)

# ponto1 = Point(int(input('Coordenada x: ')), int(input('Coordenada y: ')))
# ponto2 = Point(int(input('Coordenada x: ')), int(input('Coordenada y: ')))
# print('\nDistância da oridem: {}\nDistância entre pontos: {}'.format(ponto1.distanceOrigin(), ponto1.distancePoints(ponto2)))
# ponto1._x = 3
# print(ponto1.getX())
