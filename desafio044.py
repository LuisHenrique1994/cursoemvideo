print('{:=^40}'.format(' LOJAS TREVE '))
preço = float(input('Insira o valor das compras: R$'))
print('''
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a sua opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parceçada {} de R${:.2f} com juros de 20%.'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
