def somatorio(vet):
    resultado = 0
    for i in range(0, len(vet)):
        resultado += int(vet[i])
    print(resultado / len(vet))

somatorio(input("Somatório: ").split(" "))