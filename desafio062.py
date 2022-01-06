# Melhorando programa 061 opções de continuar contando termos ou parar

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim!')
print('Progressão finalizada com {} termos mostrados.'.format(total))
