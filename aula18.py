# Listas (parte 2) exemplo 1

teste = []  # Criando lista vazia chamada teste
teste.append('Henrique')  # adicionando "henrique na lista 'teste'"
teste.append(26)  # adicionando idade '26' a henrique
galera = []  # Criando lista vazia chamada galera
galera.append(teste[:])  # criando uma copia da lista teste dentro da lista galera
teste[0] = 'Gustavo'  # na lista teste na posição 0 recebe o nome "Gustavo"
teste[1] = 40  # na lista teste na posição 1 recebe numero 40
galera.append(teste[:])  # criando copia da lista teste dentro da lista galera
print(galera)

print('=' * 30)

# Exemplo 2

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # criando lista de pessoas + idades
print(pessoas[2][1])  # na lista pessoas na posição 2 mostrar item 1
print(pessoas[0][0])  # na lista pessoas na posição 0 mostrar item 0
print(pessoas[3])  # na lista pessoas mostrar item 3

print('=' * 30)

# Exemplo 3

for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')  # para cada pessoas em pessoas mostrar item 0 e item 1

print('=' * 30)

moçada = list()  # criando lista vazia chamada moçada usando "list()"
dado = list()  # criando lista vazia chamada dado usando "list()"

for c in range(0, 3):  # conte de 0 a 2, peça nome(str) e idade(int) e adicione a lista dado
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    moçada.append(dado[:])  # em moçada crie uma copia da lista dado
    dado.clear()  # limpe a lista dado

print(moçada)

totmai = totmen = 0  # iniciando duas variaves (int) em 0
for p in moçada:  # para cada pessoa em moçada
    if p[1] >= 21:  # Se o item 1(idade) em pessoa for maior ou igual a 21
        print(f'{p[0]} é maior de idade.')  # mostre a posição 0
        totmai += 1  # some 1 na variavel total de maiores
    else:  # se não
        print(f'{p[0]} é menor de idade.')  # mostre posiçao 0
        totmen += 1  # some 1 na variavel total de menores
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
