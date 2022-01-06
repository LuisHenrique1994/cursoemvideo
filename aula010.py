'''nome = str(input('Qual é o seu nome? '))
if nome == 'Henrique':
    print('Que nome lindo você tem!')
else:
    print('Que nome legal você tem!')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.2f}'.format(m))
#print('Parabéns!' if m >=6.0 else 'Estude mais!')
if m >= 6.0:
    print('Parabéns você foi aprovado!')
else:
    print('Infelizmente você foi reprovado!')
