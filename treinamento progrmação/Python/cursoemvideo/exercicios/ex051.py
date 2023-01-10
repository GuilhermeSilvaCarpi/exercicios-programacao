# aula 13
print('*'*25)
print('10 termos de uma PA'.center(25))
print('*'*25)

priterm = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimoterm = priterm + 10 * razão

for i in range(priterm, decimoterm, razão):
    print(i, end=' -> ')
print('ACABOU')
