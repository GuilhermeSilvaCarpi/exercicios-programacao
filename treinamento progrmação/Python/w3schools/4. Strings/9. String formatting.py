# metodo format
firstname = 'Guilerme'
lastname = 'Carpi'
print('nome: {}'.format('{} {}'.format(firstname, lastname)))

# indexs numerados
complitename = '{0} {1}'.format(firstname, lastname)

age = 17
print('conhece {0}? {0} tem {1} anos de idade'.format(firstname, age))

# indexs nomeados
print('eu vou querer um {entrada}, depois um {pratoprincipal}, e no final {sobremesa}'.format(
entrada = 'pastel', pratoprincipal = 'arroz com feijão', sobremesa = 'sorvete'))
