num = int(input('Digite um numero qualquer: '))
resultado = num % 2
#o resto da divisão de qualquer numero PAR por 2 é igual a 0
#o resta da divisão de qualquer numero ÍMPAR por 2 é igual a 1
if resultado == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número  {} é ÍMPAR'.format(num))
