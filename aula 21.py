# Estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
# escopo de variáveis e retorno de resultados.

# Exemplo 1 (interactive help)
help(print)  # Mostra a definição de funções built-in e suas possíveis variações(parâmetros opcionais) com explicações.


# Exemplo 2 (docstrings)
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Luis Henrique Treve Nunes em 31/08/2021 às 15:34hs horário de UK.
    """  # essa é a "docstring" da função contador
    c = i
    while c <= f:
        print(f'{c} ', end='')
    print('FIM!')


help(contador)  # O comando help() + a função non Built-in 'contador' como argumento você verá a docstring de contador


# Exemplo 3 (parâmetros opcionais)
def somar(a=0, b=0, c=0):  # a=0 é um parâmetro opcional, se o usuário nao digitar um valor para a, então será 0
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Luis Henrique Treve Nunes em 31/08/2021 às 15:41hs horário de UK.
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2)
somar(3, 2, 5)  # No caso foi definido somente 3 parâmetros,digitando mais que 3 dará erro. opção usar def somar(* nums)
somar(3)


# Exemplo 4 (escopo de variáveis -> valores dentro e/ou fora de funções)
def função():
    n1 = 4
    print(f'\nN1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fora vale {n1}')
