# Copiando uma lista
"""Se escrevermos que uma lista é igual a outra, essa
vai será uma referência a outra, não um lista nova
com os mesmos valores"""
lista = [2, 4, 5, 3, 6]
print(lista)
lista2 = lista
lista2.pop(-1)
print(lista)
print()

## Método 'copy()'
"""Essa situação pode ser evitada utilizando o método
de lista 'copy'"""
lista3 = lista.copy()
lista3.pop(0)
print(lista)
print(lista3)
print()

## Método próprio 'list()'
lista4 = list(lista)
lista4.pop(1)
print(lista)
print(lista4)
print()
