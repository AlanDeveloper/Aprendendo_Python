class Triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def equilatero(self):
        return True if self.p1 == self.p2 and self.p1 == self.p3 else False
    def isosceles(self):
        teste1 = True if self.p1 == self.p2 and self.p1 != self.p3 else False
        teste2 = True if self.p1 == self.p3 and self.p1 != self.p2 else False
        teste3 = True if self.p2 == self.p3 and self.p2 != self.p1 else False
        return teste1 or teste2 or teste3
    def escaleno(self):
        teste1 = True if self.p1 != self.p2 else False
        teste2 = True if self.p1 != self.p3 else False
        teste3 = True if self.p3 != self.p2 else False
        return teste1 and teste2 and teste3

    def perimetro(self):
        return self.p1 + self.p2 + self.p3

obj1 = Triangulo(1, 1, 1)
obj2 = Triangulo(2, 1, 1)
obj3 = Triangulo(2, 1, 3)
print(obj1.equilatero(), obj2.isosceles(), obj3.escaleno(), obj1.perimetro())
print(obj2.equilatero(), obj3.isosceles(), obj1.escaleno(), obj2.perimetro())
print(obj3.equilatero(), obj1.isosceles(), obj2.escaleno(), obj3.perimetro())