n1: str
while not n1.isnumeric():
    n1 = (input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('A soma de {} e {} é igual a {}'.format(n1, n2, n1 + n2))
