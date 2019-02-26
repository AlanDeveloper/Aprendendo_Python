def invertido(number):
    number *= number
    number = str(number)
    return number[::-1]

invertido(int(input("Quadrado invertido: ")))