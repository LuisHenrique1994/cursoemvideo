n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Média abaixo de 5.0: Reprovado!')
    print('Sua media foi {} e infelizmente você foi reprovado.'.format(media))
elif media <= 6.9:
    print('Média entre 5.0 e 6.9: Recuperação!')
    print('Sua média foi {} e você está de recuperação.'.format(media))
elif media >= 7:
    print('Média igual 7.0 ou superior: Aprovado!')
    print('Parabéns sua média é {} e você está Aprovado.'.format(media))
