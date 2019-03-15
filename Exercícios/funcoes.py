# Matriz Transposta
def matrizTransposta(matriz, line, col):
    if len(matriz) != line*col:
        print('Números insuficientes')
    else:
        matriz = matriz.split(',')
        for i in len(matriz):
            
        print(matriz.split(','))

matrizTransposta(input('Informe a matriz(através de ","): '), int(input('Linhas: ')), int(input('Colunas: ')))