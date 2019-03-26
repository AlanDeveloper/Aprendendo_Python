def divisao(x, y):
    try:
        return float(x) / float(y)
    except ValueError as Vr:
        print('Digite um inteiro')
        raise Vr
    except ZeroDivisionError as Zd:
        print('Não é possível divisão por zero')
        raise Zd

def main():
    while True:
        x = input('Digite um valor: ')
        y = input('Digite um valor: ')
        try:
            z = divisao(x, y)
        except BaseException:
            print('Tente de novo\n')
        else: 
            print(z)
            break

if __name__ == "__main__":
    main()
