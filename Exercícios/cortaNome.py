def corta(name):
    name = name.split(" ")
    number = len(name)
    abrevia = ""
    i = 0
    while i < number:
        if i == 0 or i == number - 1:
            abrevia += name[i]
        else:
            abrevia += ' ' + name[i][0] + '. '
        i += 1
    print(abrevia)

corta(str(input("Abreviar nome: ")))