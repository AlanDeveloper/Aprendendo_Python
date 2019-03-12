def primo(valor):
    if valor > 3 and (valor % 2 == 0 or valor % 3 == 0):
        print('Não é primo!')
    else:
        print('É primo!')

primo(int(input("Teste se é primo: ")))