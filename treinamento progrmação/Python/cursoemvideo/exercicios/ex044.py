# aula 12
# inputs
preçoinicial = float(input('Preço das compras: R$'))
print('-'*30)
resp = int(input('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção?'''))
print('-'*30)
preço = preçoinicial
# outputs
if resp == 1:
    preço = preçoinicial - (preçoinicial / 100 * 10)
elif resp == 2:
    preço = preçoinicial - (preçoinicial / 100 * 5)
elif resp == 3:
    print('A compra será parcelada em 2x de R${} SEM JUROS'.format(preçoinicial / 2))
elif resp == 4:
    parcelas = int(input('Quantas parcelas? '))
    preço = preçoinicial  + (preçoinicial / 100 * 20)
    print('A compra será parcelada em {}x de {} COM JUROS'.format(parcelas, preço / parcelas))
else:
    preço = 0
    print('OPÇÃO INVALIDA DE PAGAMENTO')
print('A compra de R${} vai custar R${} no final'.format(preçoinicial, preço))