import math
ang = float(input('Digite o valor de um ângulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Para o ângulo {} temos seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}.'.format(ang, sen, cos, tan))
