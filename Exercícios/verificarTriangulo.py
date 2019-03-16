from classeTriangulo import Triangulo
# import classeTriangulo as trian

def verificarTriangulo(lado1, lado2, lado3):
    teste1 = lado1 - lado2 < lado3 and  lado3 < lado1 + lado2
    teste2 = lado1 - lado3 < lado2 and  lado2 < lado1 + lado3
    teste3 = lado3 - lado2 < lado1 and  lado1 < lado3 + lado2
    triangulo = Triangulo(lado1, lado2, lado3)
    tipo = 'equilatero' if triangulo.equilatero() else 'escaleno' if triangulo.escaleno() else 'isosceles'
    return 'É um triângulo ' + tipo + '!!!' if teste1 and teste2 and teste3 else 'Não é um triângulo.'

print(verificarTriangulo(int(input('Primeira coordenada: ')), int(input('Segunda coordenada: ')), int(input('Terceira coordenada: '))))