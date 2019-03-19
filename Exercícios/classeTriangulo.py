class Triangulo:
    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
    
    def _equilatero(self):
        return True if self._p1 == self._p2 and self._p1 == self._p3 else False
    def _isosceles(self):
        teste1 = True if self._p1 == self._p2 and self._p1 != self._p3 else False
        teste2 = True if self._p1 == self._p3 and self._p1 != self._p2 else False
        teste3 = True if self._p2 == self._p3 and self._p2 != self._p1 else False
        return teste1 or teste2 or teste3
    def _escaleno(self):
        teste1 = True if self._p1 != self._p2 else False
        teste2 = True if self._p1 != self._p3 else False
        teste3 = True if self._p3 != self._p2 else False
        return teste1 and teste2 and teste3

    def _perimetro(self):
        return self._p1 + self._p2 + self._p3


obj1 = Triangulo(1, 1, 1)
obj2 = Triangulo(2, 1, 1)
obj3 = Triangulo(2, 1, 3)
print(obj1._equilatero(), obj2._isosceles(), obj3._escaleno(), obj1._perimetro())
print(obj2._equilatero(), obj3._isosceles(), obj1._escaleno(), obj2._perimetro())
print(obj3._equilatero(), obj1._isosceles(), obj2._escaleno(), obj3._perimetro())