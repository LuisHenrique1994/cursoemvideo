nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Treve':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil {}.'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
