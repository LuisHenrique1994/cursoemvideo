# Cadastrando pessoas e dizendo total de pessoas , total de homens e total de mulheres com menos de 20 anos

total18 = totalh = totalm20 = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        total18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totalm20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totalh} homens cadastrados')
print(f'Temos {totalm20} mulheres com menos de 20 anos')
print('ACABOU')
