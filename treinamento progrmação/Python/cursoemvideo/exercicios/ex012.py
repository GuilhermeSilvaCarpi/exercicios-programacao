#aula 7
preco_produto = float(input('Um preço de produto: R$'))
preco_desconto = preco_produto * 5 / 100

#       preco_produto       100
#             x              5
print('R${} com 5% de desconto = R${:.2f}'
	    .format(preco_produto,preco_produto-preco_desconto))
