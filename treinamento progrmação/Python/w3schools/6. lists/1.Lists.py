# Listas
umalista = ['str 1', 'str 2', 'str 3']
listadefrutas = ['banana', 'uva', 'pera']

print(umalista)
print(listadefrutas)

# Listas são ordenadas, mutaveis e permitem itens duplicados
# A função len() retorna alargura de uma lista, ou, a quantidade de itens nela
print('a largura da lista de frutas é {}'.format(len(listadefrutas)))

# Uma lista pode ter diferentes tipos de dados, inclusive juntos em uma mesma lista
# O tipo/classe de dado da lista é "list"
print(type(umalista))

# É possivel fazer listas usando "metodo construtor"
listadenumeros = list((654, 345, 435, 8766, 7654))
print(listadenumeros)