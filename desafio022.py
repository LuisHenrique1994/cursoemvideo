nome = str(input('Nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
letras = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(letras[0], len(letras[0])))