# aula 13
print('Digite seis números a seres somados:')
soma = 0
somapares = 0
somaimpares = 0
quantpares = 0
quantimpares = 0
print()
for i in range(1, 7):
    n = float(input('{}° numero: '.format(i)))
    soma += n
    if n % 2 == 0:
        somapares += n
        quantpares += 1
    else:
        somaimpares += n
        quantimpares += 1 
print()
print('A soma dos todos números digitados é: {}'.format(soma))
print('A soma dos {} número(s) pares digitados é: {}'.format(quantpares, somapares))
print('A soma dos {} número(s) impares digitados é: {}'.format(quantimpares ,somaimpares))
