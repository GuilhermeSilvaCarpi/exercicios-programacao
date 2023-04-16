print('Compreensão de lista')

print('-'*40)
print('sintax:')
# [comando/ for item in iterador / extrutura condicional]
lista = ['13', '15', '19', '23', '25', '29']
[print(item, end=' ') for item in lista if '1' in item]

print()
print('-'*40)
print('''A extrutura condicional não é
obrigatória''')
[print(item, end=' ') for item in lista]
