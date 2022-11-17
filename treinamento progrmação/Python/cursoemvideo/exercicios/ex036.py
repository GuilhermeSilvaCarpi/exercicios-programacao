#aula 12

#inputs
vCasa = float(input('valor de casa pra comprar: '))
vSalario = float(input('salário de um hipotético comprador: '))
quantosAnos = int(input('anos de financiamento da casa: '))

#calculo prestação
prestacao = vCasa / (quantosAnos * 12)

print('para pagar uma casa de R${:.2f} em {} anos a prestação da casa será de R${:.2f}'.format(vCasa,quantosAnos,prestacao))

#aprovação da compra
print('emprestimo aprovado'if prestacao <= (vSalario / 100 * 30) else'emprestimo negado')
