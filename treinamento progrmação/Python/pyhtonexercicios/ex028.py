from random import randint
n = randint(1, 5)
c = int(input('chute um numero de 1 a 5'))
if c == n:
    print('pensamos no mesmo numero')
else:
    print('eu pensei em {} e vc em {}'.format(n, c))
print('fin')
