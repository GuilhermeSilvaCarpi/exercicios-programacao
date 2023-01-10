# aula 13
soma = 0
quantidade = 0
'''for i in range(3, 501, 3): 
    #print(i, end=' ')
    s += i
    quantidade += 1
print()
print('A soma entre todos os números múltiplos de 3 e entre 1 e 500 é: {}'.format(s))
print(quantidade)'''
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i # acumulador
        quantidade += 1 # contador
        # print(i, end=' ')
print('A soma dos {} tantos valores solicitados resultou em: {}'.format(quantidade, soma))
