# Par ou Ímpar com o computador

from random import randint

print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')

cont = 0
while True:
    print('=-=' * 10)

    player_value = int(input('Diga um valor: '))
    computer_value = randint(0, 10)
    total = player_value + computer_value

    player_choice = ' '
    while player_choice not in 'PI':
        player_choice = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 35)
    print(f'Você jogou {player_value} e o computador {computer_value}. Total de {total} ', end='')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    print('-' * 35)

    if player_choice == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break

    elif player_choice == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
