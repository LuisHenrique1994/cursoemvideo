# Ler nome e preço de produtos, mostrar total de gastos, quantos custam + de 1k e o nome do produto mais barato

totcompra = tot1000 = menor = cont = 0
barato = ''
while True:

    product = input('Nome do Produto: ')
    price = float(input('Preço: R$ '))
    cont += 1
    totcompra += price

    if price > 1000:
        tot1000 += 1
    if cont == 1 or price < menor:
        menor = price
        barato = product

    resp = ' '
    while resp not in 'SN':
        resp = (input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi R$ {totcompra:4.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
print(f'{"FIM DO PROGRAMA":-^40}')
