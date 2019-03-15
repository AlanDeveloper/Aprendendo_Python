class Pessoa:
    def __init__(self, nome, dtNascimento, tel):
        self.nome = nome
        self.dtnascimento = dtNascimento
        self.telefone = tel
    
    def __str__(self):
        return "Olá, meu nome é %s\nData de nascimento: %s\nTelefone: %s" % (self.nome, self.dtnascimento, self.telefone)

    def setNome(self, nome):
        self.nome = nome
    def setdtNascimento(self, dtNascimento):
        self.dtnascimento = dtNascimento
    def setTel(self, tel):
        self.telefone = tel
    
    def getNome(self):
        return self.nome
    def getdtNascimento(self):
        return self.dtnascimento
    def getTel(self):
        return self.telefone

obj = Pessoa(input("Informe seu nome: "), input("Informe sua data de nascimento: "), input("Informe seu telefone: "))
print(obj.__str__())