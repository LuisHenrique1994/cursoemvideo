# Progressão aritmética usando while para 10 termos

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    contador += 1
print('Fim!')
