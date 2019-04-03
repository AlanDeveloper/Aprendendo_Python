import datetime

class Person:
    def __init__(self, name, birth, phone):
        self._name = name
        self._birth = None
        self._phone = phone
   
        self.setBirth(birth)
    
    def __str__(self):
        return "\nNome: {}\nData de nascimento: {}\nTelefone: {}".format(self._name, self._birth, self._phone)

    def getName(self): return self._name
    def getBirth(self): return self._birth
    def getPhone(self): return self._phone

    def setName(self, name): self._name = name
    def setBirth(self, birth): 
        birth = birth.split('-')
        self._birth = datetime.date(int(birth[2]), int(birth[1]), int(birth[0]))
    def setPhone(self, phone): self._phone = phone

    name = property(getName, setName)
    birth = property(getBirth, setBirth)
    phone = property(getPhone, setPhone)

obj = Person(input("Informe seu nome: "), input("Informe sua data de nascimento(dd-mm-yyyy): "), input("Informe seu telefone: "))
print(obj.__str__())

obj.setName('Julio')
print(obj.__str__())
