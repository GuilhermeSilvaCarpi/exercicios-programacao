print('Adicionando itens em listas')
lista = ['a', 'e', 'i', 'o', 'u']
print(lista)

print('-'*40)
print('''Método [append()]. Adiciona um item no
final da lista.''')
lista.append('ão')
print(lista)

print('-'*40)
print('''Método [insert()]. Insere um item em uma
posição específica da lista.''')
lista.insert(2, 3)
print(lista)

print('-'*40)
print('''Método [extend()]. Acrescenta uma lista
no final de outra.''')
lista = ['a', 'e']
lista2 = ['i', 'o', 'u']
print('lista:', lista)
print('lista2:', lista2)
lista.extend(lista2)
print(lista)

print()
print('''O método [extend()] pode adicionar
qualquer tipo de iterável a uma lista.''')
lista = ['a', 'b', 'c']
tuple = ('d', 'e', 'f')
print('lista:', lista)
print('tuple:', tuple)
lista.extend(tuple)
print('''lista
  |
  V''')
print(lista)

