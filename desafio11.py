h = float(input('Digite altura em metros: '))
b = float(input('Digite largura em metros: '))
a = b * h
t = a / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(h, b, a))
print('Para pintar essa parede você irá precisar de {} litros de tinta.'.format(t))
