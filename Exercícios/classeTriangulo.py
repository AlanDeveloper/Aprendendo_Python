class Triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def equilatero(self):
        return True if self.p1 == self.p2 and self.p1 == self.p3 else False
    def isosceles(self):
        teste1 = True if (self.p1 == self.p2 and self.p1) != self.p3
        teste2 = True if (self.p1 == self.p2 and self.p1 != self.p3
        teste3 = True if (self.p1 == self.p2 and self.p1) != self.p3
        return True if self.p1 == self.p2 and self.p1 != self.p3

obj = Triangulo(1, 1, 1)
print(obj.equilatero())