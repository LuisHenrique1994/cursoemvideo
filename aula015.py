# Interrompendo repetições while

n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')

# "f string" inserida, ou seja, print formatado, todas as formatações continuam funcionando porém facilitado com o print(f'text')
