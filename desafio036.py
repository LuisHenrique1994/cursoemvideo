print('Bem vindo ao Treve Crédit, impréstimos imobiliários, vamos calcular o seu impréstimo.')
casa = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira o seu salário mensal: R$'))
anos = int(input('Inisira em quantos anos deseja pagar: '))
parcela = casa / (anos * 12)
if parcela <= salario * 30 / 100:
    print('-=-' * 25)
    print('Para pagar uma casa de R${:.2f} em {} anos sua parcela será de R${:.2f}.'.format(casa, anos, parcela))
    print('Párabens, impréstimo aprovado!')
else:
    print('-=-' * 25)
    print('Para pagar uma casa de R${:.2f} em {} anos, sua parcela será de R${:.2f}.'.format(casa, anos, parcela))
    print('É necessário que a sua parcela seja igual ou inferior 30% do seu salário.')
    print('Infelizmente o seu impréstimo negado!')
