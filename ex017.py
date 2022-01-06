from math import hypot
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa é {:.2f}'.format(hypot(cato, cata)))

'''modo matematico para fazer: >>hi = (cato ** 2 + cata ** 2) ** (1/2)<<#
variavel hi , somando os catetos ao quadrado elevando a meio ou seja tirando a raiz quadrada.'''