print('removendo itens de listas')
lista = ['a', 'e', 'i', 'o', 'u']
print(lista)

print('-'*40)
print('''Método [remove()]. Remove um item
expecificado no parâmetro.''')
lista.remove('i')
print(lista)

print('-'*40)
print('''Método [pop()]. Remove o item de um
index expecíicado.''')
lista.pop(1)
print(lista)
print('''Se um index não for específicado, o
método [pop()] irá tirar o ultimo item.''')
lista.pop()
print(lista)

print('-'*40)
print('Palavra chave [del]. Deleta variáveis.')
del lista[0]
print(lista)
print('''O [del] também pode excluir uma lista
por inteira.''')
del lista

print('-'*40)
print('Método [clear]. Limpa a lista')
lista2 = ['a', 'b', 'c', 'd']
print('antes:', lista2)
lista2.clear()
print('depois:', lista2)
