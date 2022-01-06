# While True com break

soma = quantidade = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    quantidade += 1
    soma += valor
print(f'A soma dos {quantidade} valores foi {soma}!')
print('Programa finalizado com sucesso!')
