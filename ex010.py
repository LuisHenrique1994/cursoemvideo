real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.37
dolardovideo = real / 3.27
libra = real / 7.22
euro = real / 6.42
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você podia comprar US${:.2f} (na época do vídeo.)'.format(real, dolardovideo))
print('Com R${:.2f} você pode comprar GBP£{:.2f}'.format(real, libra))
print('Com R${:.2f} você pode comprar EUR€{:.2f}'.format(real, euro))
