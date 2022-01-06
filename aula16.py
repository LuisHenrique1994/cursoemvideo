# Tuplas

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Alface', 'Cebola', 'Batata'
print(f'Temos {len(lanche)} items no menu\n')

# Sorted mostra lista em ordem alfabética
print(sorted(lanche))
print('\n')

# Acessando elementos da tupla(lists or dictionarys) em maneiras diferentes

# Exemplo 1 (mais simples e indicado quando não precisa da posição do item)
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('\n')

# Exemplo 2 (mais indicado quando precisa da posicao do item "contador")
for contador in range(0, len(lanche)):
    print(f'Eu Vou comer {lanche[contador]} na posição {contador}')

print('\n')

# Exemplo 3
for contador, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {contador}')


print("\nTava com fome mesmo.")
