#aula 10
n1 = float(input("um numero:    "))
n2 = float(input("outro numero: "))
n3 = float(input("outro numero: "))
maiorImputN = float
menorImputN = float

#verificando menor input
maiorImputN = n1
if n2 > n1 and n2 > n3:
    maiorImputN = n2
elif n3 > n1 and n3 > n2:
    maiorImputN = n3

#verificando maior input
menorImputN = n1
if n2 < n1 and n2 < n3:
    menorImputN = n2
elif n3 < n1 and n3 < n2:
    menorImputN = n3

#saidas
print('o menor input dos numeros foi: {}'.format(menorImputN))
print('o maior input dos numeros foi: {}'.format(maiorImputN))
