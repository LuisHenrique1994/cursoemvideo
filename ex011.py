b = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))
a = b * h
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(b, h, a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(a / 2))
