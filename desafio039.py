from datetime import date
nascimento = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    print('Em {} anos você deve se alistar ao serviço militar.'.format(18 - idade))
elif idade == 18:
    print('Este na hora, você de se alistar ao serviço militar neste ano de {}.'.format(date.today().year))
else:
    print('Já se passaram {} anos do seu alistamento militar.'.format(idade - 18))
print('Você atualmente tem {} de idade.'.format(date.today().year - nascimento))
