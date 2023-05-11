'''
Como usar listas como arrays
Isso exigira a importação de uma bibliotéca
Arrays armazenam muitos dados em uma variável
'''

# 1. Criando uma lista e assessando os itens dela
nomes = ['Gustavo', 'Dários', 'Alessandra', 'Andressa']
print(nomes[0], nomes[2])

# 2. Modificando um item da lista
nomes[1] = 'Jorge'
print(nomes)

# 3. É possível obter a quantidade de itens em um array com o método "len()"
print('Largura da lista:', len(nomes))
'''Nota: a largura da lista é um númer maior do que o index do último item
(por causa que o primeiro item tem o index 0)'''

# 4. Loop pelos itens de uma lista
for nome in nomes:
    print('__', nome)

# 5. Adicionando item a uma lista
'''Isso pode ser feito usando o método "append()" '''
nomes.append('Carla')
print(nomes)

# 6. Removendo itens de uma lista
# 6.1. Usando o método "pop()"
'''Este método remove um item a partir do index dele'''
nomes.pop(3)
print(nomes)

# 6.2. Usando o método "remove()"
'''Este método remove um item igual ao que está entre parenteses
Se tiver mais de um, o item retirado será o primeiro igual o especificado'''
nomes.remove('Carla')
print(nomes)

# Além desses há vários outros métodos disponiveis para serem usados em listas
