#aula 10
from math import sqrt
r1 = float(input('um comprimento de reta: '))
r2 = float(input('outro comprimento de reta: '))
r3 = float(input('outro comprimento de reta: '))

'''print('as retas {}, {} e {}'. format(r1,r2,r3),
      'podem'if r1 > sqrt((r2 - r3)*(r2 - r3)) and r1 < (r2+r3) else'não podem',
      'formar um triângulo')'''

print('as retas {}, {} e {}'.format(r1,r2,r3),
      'podem'if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2) else'não podem',
      'formar um triâmgulo')
