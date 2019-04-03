def getDict(nome, dt, tel):
    d = { 'nome': nome, 'dataNascimento': dt, 'telefone': tel }
    print('\nNome: ' + d.get('nome') + '\nData de nascimento(DD-MM-YYYY): ' + d.get('dataNascimento') + '\nTelefone: ' + d.get('telefone'))


nome = input("Informe seu nome: ")
dataNascimento = input("Informe sua data de nascimento: ")
telefone = input("Informe seu telefone: ")
getDict(nome, dataNascimento, telefone)