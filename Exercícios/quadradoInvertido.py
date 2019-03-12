def invertido(number):
    number *= number
    number = str(number)
    print(number[::-1])

invertido(int(input("Quadrado invertido: ")))