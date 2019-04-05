class Person:
    def __init__(self, name, age, height, weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
    
    def birthDay(self): self._age += 1
    def loseWeight(self, weight): self._weight -= weight
    def fattening(self, weight): self._weight += weight
    def grow(self, height):  self._height += height
    def __str__(self): return 'Nome: {}, Idade: {}, Altura: {}, Peso: {}'.format(self._name, self._age, self._height, self._weight)

    def getName(self): return self._name
    def getAge(self): return self._age
    def getHeight(self): return self._height
    def getWeight(self): return self._weight

    def setName(self, name): self._name = name
    def setAge(self, age): self._age = age
    def setHeight(self, height): self._height = height
    def setWeight(self, weight): self._weight = weight

    name = property(getName, setName)
    age = property(getAge, setAge)
    height = property(getHeight, setHeight)
    weight = property(getWeight, setWeight)


p1 = Person('Maurício', 18, 162, 59)
p2 = Person('Alan', 18, 183, 70)

p1.birthDay()
p2.fattening(10)
p1.loseWeight(5)
p1.grow(2)

print(p1.__str__(), p2.__str__())