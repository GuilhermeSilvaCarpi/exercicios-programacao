# aula 13
n = int(input('Digite um número: '))
divisões = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisões += 1
        print('\033[33m({})'.format(i), end=' ')
    else:
        print('\033[34m{}'.format(i), end=' ')

print('\n\033[mO número {} foi divisível \033[33m{}\033[m vezes'.format(n, divisões))
if divisões == 2:
    print('E por isso É PRIMO')
else:
    print('E por isso NÃO É PRIMO')
