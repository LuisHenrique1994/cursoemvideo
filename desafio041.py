from datetime import date
nascimento = int(input('Data de nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('Sua idade é {} portanto sua categoria é Mirim.'.format(idade))
elif idade <= 14:
    print('Sua idade é {} portanto sua categoria é Infantil.'.format(idade))
elif idade <= 19:
    print('Sua idade é {} portanto sua categoria é Junior.'.format(idade))
elif idade <= 20:
    print('Sua idade é {} portanto sua categoria é Sênior.'.format(idade))
else:
    print('Sua idade é {} portanto sua categoria é Master.'.format(idade))
