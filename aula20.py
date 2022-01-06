#  Funções -> modo de simplificar definindo uma função para linhas de códigos repetidos

def linha():
    print('-' * 20)


# Exemplo 1
def título(txt):
    print('-' * 30)
    print(txt)


# Programa principal
título('Curso em Vídeo')
título('Aprenda python')


linha()
# Exemplo 2
# código repetindo
a = 4
b = 5
s = a + b
print(s)

a = 9
b = 8
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

linha()


# Usando uma função para as operações a cima
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
print('-' * 20)
soma(a=9, b=8)  # Explicitando posição dos parâmetros
print('-' * 20)
soma(b=2, a=1)  # Invertendo a posição dos parâmetros

linha()
# Exemplo 3
# Empacotando diversos parâmetros na função(quantos forem necessários.)


def contador(* numeros):
    tamanho = len(numeros)
    print(f'Recebi os valores {numeros} e são ao total {tamanho} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

linha()
# Exemplo 4
# Passando lista como parâmetro e manipulando valores(dobrando valores no caso)


def dobra(minhalista):
    posição = 0
    while posição < len(minhalista):
        minhalista[posição] *= 2
        posição += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)

dobra(valores)
print(valores)
