print('-=-' * 21)
print('Analisador de triângulos')
print('-=-' * 21)
r1 = float(input('Insira o primeiro comprimento de reta: '))
r2 = float(input('Insira o segundo comprimento de reta: '))
r3 = float(input('Insira o terceiro comprimento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo!')
    if r1 == r2 == r3:
        print('Este triângulo é equilátero, todos os seus lados são iguais.')
    elif r1 == r2 and r1 != r3:
        print('Este triângulo é isósceles, dois lados são iguais.')
    elif r1 == r3 and r1 != r2:
        print('Este triângulo é isósceles, dois lados são iguais.')
    elif r2 == r3 and r2 != r1:
        print('Este triângulo é isósceles, dois lados são iguais.')
    else:
        print('Este triângulo é escaleno, todos os lados são diferentes.')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')

# resolução do exercício pelo guanabara
'''if r1 == r2 == r3:
    print('equilátero')
elif r1 != r2 != r3 != r1:
    print('escaleno')
else:
    print('isósceles')'''
