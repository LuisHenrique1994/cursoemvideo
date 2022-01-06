#a = 3
#b = 5
#print('Os valores são \033[4;32m{}\033[m e \033[4;31m{}\033[m !'.format(a, b))

nome = str(input('Qual seu nome? ')).strip()
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[31m', nome, '\033[m'))
