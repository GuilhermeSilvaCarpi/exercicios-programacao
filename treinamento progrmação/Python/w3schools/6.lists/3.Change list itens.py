larg = 35

def titulo(titu: str):
	print('_'*larg)
	print(titu.center(larg))
	print('`'*larg)

# lista
titulo('lista')
lista = ['ana', 'ena', 'ina', 'ona', 'una']
print(lista)
print('''

''')

#  mudando item de lista
titulo('mudando um item de lista')
lista[2] = 'ini'
print(lista)
print('''

''')

# intervalo de lista
titulo('intervalo de lista')
print(lista[:3])
print(7*' ', end='')
print(lista[1: 4])
print(14*' ', end='')
print(lista[2:])
print('''

''')

# mudando um intevalo de itens
titulo('mudando intervalo de itens')
lista[1:3] = ['e__', 'i__']
print(lista)
print('''

''')

# mudando quantidade de itens
titulo('mudando quantidade de itens')
print("""A largura da lista vai mudar se: a
quantidade de itens inseridos for
diferente da quantidade de itens
substituidos.""")
lista = ['a', 'e', 'i', 'o', 'u']
print(lista)
lista[1:3] = [1, 2, 3, 4]
print(lista)
lista[1:5] = ['ei']
print(lista)
lista[1:2] = ['e', 'i']
print('''

''')

# inserindo itens
titulo('inserindo itens')
print(lista)
print('''O método [insert()] insere um item
em um posição específicada, sem
precisar substituir algum item''')
lista.insert(4, '0')
print(lista)
