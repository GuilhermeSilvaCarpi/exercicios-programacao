#aula 10
from random import randint

nAleatorio = randint(0, 5)
nInput = int(input('um numero inteiro entre 0 e 5: '))
print('o numero de input é', 'igual'if nInput == nAleatorio else'diferente' ,'o numero aleatório!')
print('numero de input:  {}'.format(nInput))
print('numero aleatório: {}'.format(nAleatorio))
