#aula 07
d     =   int(input('dias q o carro foi alugado: '))
km    = float(input('km percorridos por um carro alugado: '))
preco = (60 * d) + (0.15 * km)
print('O aluguel desse carro tá custanto R${:.2f}'.format(preco))
 