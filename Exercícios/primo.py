def primo(valor):
    if valor > 3 and (valor % 2 == 0 or valor % 3 == 0):
        return False
    else:
        return True

primo(int(input("Teste se é primo: ")))