lista = ['aa', 'bb', 'ab', 'ba', 'ca', 'cc', 'cb', 'bc', 'ac']
listaNum = [123, 43 ,554, 54,23, 2,342, 34,23]
print(lista)

# Organização alfanumérica e crescente
"""Os objetos de lista tem o método 'sort()', que
faz isso automáticamente, editando a lista"""
lista.sort()
listaNum.sort()
print(lista)
print(listaNum)
print()

# Organização decrescente
"""Adicionando o parâmetro 'reverse = True' ao
método sort, ele fará a lista ficar em ordem
decrescente"""
lista.sort(reverse = True)
listaNum.sort(reverse = True)
print(lista)
print(listaNum)
print()

# Customizando a função 'sort()'

# Organização independente de maiúsculas ou minúsculas
"""Sem parâmetros adicionais, a lista vai sortear
primeiro as palavras que começam com maiúsculuas,
deppois as palavras que começam com minúsculas"""
lista = ['Aa', 'bB', 'Ab', 'Ba', 'cA', 'Cc', 'cb', 'bc', 'ac']
lista.sort()
print(lista)
"""Para que isso não ocorra, nós utilizamos o
parâmetro 'key = str.lower'"""
lista.sort(key = str.lower)
print(lista)
print()

# Ordem reveresa
"""O método 'reverse()' reorganiza a lista em ordem
inversa"""
lista.reverse()
print(lista)
print()

# Revisando
"""
1. Organização alfa numérica:
    lista.sort()

2. Organização alfa numérica decrescente:
    lista.sort(reverse = True)

3. Organização independente se começa com maiúscula ou minúscula:
    lista.sort(key = str.lower)

4. Invertendo uma llista:
    lista.reverse()
"""
