# Faça uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre-o com tamanho adaptável.

def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


# Programa principal
escreva('Henrique Treve')
escreva('Curso de Python no Youtube')
escreva('LHTN')
