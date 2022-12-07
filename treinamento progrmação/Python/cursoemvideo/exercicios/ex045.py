# aula 12
from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
# inputs
jogador = int(input('''Opções de jogo:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual será a jogada? '''))

# jo ken po
delay = 0.5
sleep(delay)
print('JO',end='')
sleep(delay)
print('KEN',end='')
sleep(delay)
print('PO')
sleep(delay)

# jogadas
pc = (randint(0,2))
print('-='*12)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)

#resultados
if pc == jogador:
    print('EMPATE')
elif (pc == 0 and jogador == 1 or
      pc == 1 and jogador == 2 or
      pc == 2 and jogador == 0):
    print('VITÓRIA')
elif (jogador == 0 and pc == 1 or
      jogador == 1 and pc == 2 or
      jogador == 2 and pc == 0):
    print('DERROTA')
else:
    print('ERRO')
