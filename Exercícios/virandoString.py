def inverte(string):
    vet = string.split(" ")
    string = ""
    for i in range(0, len(vet)):
        string += vet[i][::-1] + " "
    return string

inverte(str(input("Inverter string: ")))