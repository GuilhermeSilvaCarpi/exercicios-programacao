umalista = ['uma coisa', 52, 5.8, 'uma string', 90, 'yt', True, 'somethink']
print(umalista)
print('segundo item: ', umalista[1])
print('penultimo item: ', umalista[-2])
print('intervalo de index: ', umalista[1:3])
print('a lista até o terceiro item: ', umalista[:3])
print('do quarto item em diante: ', umalista[3:])
print('intervalo de intens em negativo: ', umalista[-6:-2])
palavrachave = 'ieia'
print('há "{}" na lista'.format(palavrachave) if (palavrachave in umalista) else'não há "{}" na lista'.format(palavrachave))
