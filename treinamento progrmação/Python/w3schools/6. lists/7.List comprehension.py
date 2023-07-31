print('Compreensão de lista')
lista = ['12', '13', '15', '19', '21', '23', '25', '29']

# List comprehension
''' Usa os itens de uma lista, mas sem altera-la'''
# The syntax
'''[expressão/ for item in iterador / extrutura condicional]'''
print('-'*40)

[print(item, end=' ') for item in lista]
print()

[print(item, end=' ') for item in lista if '1' in item]
print()

algunsNumeros = [n for n in lista if '2' in n]
print(algunsNumeros)

algunsNumeros = [n for n in lista if int(n) < 24]
print(algunsNumeros)

## Expression
''' A expressão praticamente um item feito/editado com o item atual da iteração'''
algunsNumeros = [n + '__' for n in lista if int(n) < 24]
print(algunsNumeros)

''' Expressões também podem ser condições'''
algunsNumeros = [x if int(x) < 20 else x + '_' for x in lista]
print(algunsNumeros)
