print('Lista em loop')
lista = [1, 5, 10, 15, 20]
print('lista:',lista)

# Loop usando for
print('Loop for: ', end='')
for item in lista:
	print(item, end='f ')
print('''
''')

# Loop usando index em for
print('''Loop for usando index
  |
  V''')
for index in range(len(lista)):
	print('item {}: {}'.format(index, lista[index]))
print()

# Loop usando while
index = 0
print('Loop while: ', end= '')
while index < len(lista):
	print(lista[index], end='w ')
	index += 1
del index
print('''
''')

# Loop usando compresão de lista
# A menor sintaxe para percorrer uma lista
print('''Loop com compreensão de lista
  |
  V''')
[print(item, end='c ') for item in lista]

