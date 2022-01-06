# Escrevendo números por extenso a partir do input do usuário

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez')

print('Bem vindo')
while True:
    while True:
        numero = int(input('Digite um número entre 0 e 10: '))
        if 0 <= numero <= 10:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {contagem[numero]}.')

    continuar = input('Você deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print('Volte Sempre!')
