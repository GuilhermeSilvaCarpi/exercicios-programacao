print('-'*38)

for i in range(11):
    print(i, end=', ')
else:
    print('fim')

'''O objeto iterador quando criado fica
na condição que retorna o primeiro
objeto na lista (array). Quando usado o
método next, o objeto muda pra o status
pro próximo item na lista.
Um um erro é obtido se o método next
for usado mais vezes do que a
quantidade de itens na lista.'''
print('-'*38)

lista = ('banana', 'maçã', 'tomate')
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))

'''O loop for cria um objeto iterador e usa
o método next a cada passo.'''
print('-'*38)

for i in lista:
    print (i)

print('-'*38)
