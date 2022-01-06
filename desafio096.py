#  Faça uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
#  Mostre a área do terreno.

def área():
    return largura * comprimento


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
print(f'A área de um terreno {largura}x{comprimento} é de {área()}m².')
