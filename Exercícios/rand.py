import random

cond = True
numRandom = random.randint(0, 2)
tentativas = 0
while cond:
    num = int(input('Escolha um número de 0 a 1000: '))
    if num < numRandom: 
        print('Número baixo')
    elif num > numRandom:
        print('Número alto')
    else: 
        cond = False
        print('Número descoberto', '\nNúmero de tentativas:', tentativas)
    tentativas += 1