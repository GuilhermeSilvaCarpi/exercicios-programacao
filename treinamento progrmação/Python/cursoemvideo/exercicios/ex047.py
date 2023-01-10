# aula 13
print('Contagem'.center(14))
print('-'*14)
for i in range(1, 51):
    if i % 2 == 0:
        print('{:2}'.format(i), end=' ')
    if i % 10 == 0:
        print()
print('-'*14)
for i in range(2, 51, 2):
    print('{:2}'.format(i), end=' ')
    if i % 10 == 0:
        print()
print('-'*14)
