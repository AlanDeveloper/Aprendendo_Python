from math import sqrt
class Ponto:
    def __init__(self, x, y):
        self.x =  x
        self.y =  y
    
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def distanciaOrigem(self):
        distanciaX = (0 - self.x) * (0 - self.x)
        distanciaY = (0 - self.y) * (0 - self.y)
        return  sqrt(distanciaX + distanciaY)
    def distanciaEntrePontos(self, ponto):
        distanciaX = (ponto.getX() - self.x) * (ponto.getX() - self.x)
        distanciaY = (ponto.getY() - self.y) * (ponto.getY() - self.y)
        return  sqrt(distanciaX + distanciaY)

ponto1 = Ponto(int(input('Coordenada x: ')), int(input('Coordenada y: ')))
ponto2 = Ponto(int(input('Coordenada x: ')), int(input('Coordenada y: ')))
print('Distância da oridem: {}\nDistância entre pontos: {}'.format(ponto1.distanciaOrigem(), ponto1.distanciaEntrePontos(ponto2)))