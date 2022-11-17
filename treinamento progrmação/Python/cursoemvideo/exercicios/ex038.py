#aula 12
#inputs
n1 = float(input('um número: '))
n2 = float(input('outro número: '))

#ifs
if n1 > n2:
    print('o primeiro número digitado é maior que o segundo')
elif n1 < n2:
    print('o segundo número digirado é maior que o primeiro')
else:
    print('{} = {}'.format(n1, n2))
