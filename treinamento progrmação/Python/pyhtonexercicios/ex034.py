s = (float(input('Digite o salário do funvionário')))
if s > 1250:
    c = ((s / 100) * 10) + s
    print('O salário com um almento de 10% é igual a {:.2f}'.format(c))
else:
    c = ((s / 100) * 15) + s
    print('O salário com um aumento de 15% é {:.2f}'.format(c))
