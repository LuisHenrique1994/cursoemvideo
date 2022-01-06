print('--' * 18)
print('Calculador de IMC e status.')
print('--' * 18)
peso = float(input('Insira seu peso em kg: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.2f} kg/m².'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você esta no peso ideal.')
elif 25 < imc < 30:
    print('Você está com sobrepeso.')
elif 30 < imc < 40:
    print('Você está obeso.')
elif imc > 40:
    print('Você está em obesidade mórbida.')
