d = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam'.format(d, (d/1000), (d/100), (d/10)))
print('{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format((d*10), (d*100), (d*1000)))
