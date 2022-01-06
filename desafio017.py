import math
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cato, cata)
print('Hipotenusa: {:.2f}'.format(hip))
