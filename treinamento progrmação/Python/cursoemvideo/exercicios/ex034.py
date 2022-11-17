#aula 10
s = float(input('teórico salário de um funcionário: '))
if s > 1250:
    s += s / 100 * 10
else:
    s += s / 100 * 15
print('o novo salário do teórico funcionário é R${:.2f}'.format(s))
