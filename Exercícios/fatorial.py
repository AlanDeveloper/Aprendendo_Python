def fat(valor):
    resultado = 1
    while valor > 1:
        resultado = resultado * valor
        valor-= 1
    
    print(resultado if valor > 0 and valor == int(valor) else -1)

fat(int(input("Fatorial: ")))