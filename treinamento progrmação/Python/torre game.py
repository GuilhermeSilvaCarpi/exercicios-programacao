from random import shuffle
from time import sleep

#classe player
class Player():
	maxLife = 10
	life = maxLife
	
	x = 0
	y = 0
	def __init__(self):
		self.x = 1
		self.maxlife = 5

#iniciando game
cor = {'nm' : '\033[m',
       'vm' : '\033[;31m',
       'vd' : '\033[;32m',
       'am' : '\033[;33m',
       'cn' : '\033[;36m',}
player = Player()
andares = [[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]]
tesourosEncontrados = [False,False,False,False,False,False,False,False,False,False]
tesouros = ['cinturão','couraça',
            'calçados','escudo ',
            'capacete','espada',
            'oração ','perseverança',
            '','']

#radonizando andares
for andar in andares:
    shuffle(andar)
    print(andar)

#combate
def combate():
    print('um combate começou')

#tesouro encontrado
def tesouroEncontrado(index):
    if tesourosEncontrados[index] == False:
        print('{} foi encantado(a)'.format(tesouros[index]))
        tesourosEncontrados[index] = True
    else:
        print('o tesouro da sala atual já foi encontrado,\nnão há muito oque fazer aqui')

#textoTenso
def textoTenso(delay,s):
    for letra in s:
        print(letra,end='')
        sleep(delay)
    print()
#game loop
gameRunning = True
while gameRunning:
    textoTenso(0.1,'***********')
    print('{}LOCALIZAÇÃO{}\nandar : {}\nquarto: {}'.format(cor['cn'], cor['nm'],player.y, player.x + 1))
    
    #definicao de quartos
    andarPlayer = andares[player.y]
    quartoPlayer = andarPlayer[player.x]
    print('quarto atual: ',end='')
    sleep(1.25)
    
    if quartoPlayer == 1:   #quarto 1 = porta
        print(cor['vd'],end='')
        textoTenso(0.25,'escada')
        print(cor['nm'],end='')
    elif quartoPlayer == 2: #quarto 2 = inimigo
        print(cor['vm'],end='')
        textoTenso(0.25,'ameaça')
        print(cor['nm'],end='')
        combate()
    else:                   #quarto 3 = tesouro
        print(cor['am'],end='')
        textoTenso(0.25,'tesouro')
        print(cor['nm'],end='')
        tesouroEncontrado(player.y)
    sleep(2)
    
    #movimentos
    print('{}PRÓXIMO MOVIMENTO{}'.format(cor['cn'],cor['nm']))
    if player.x == 0:  #primeiro quarto do andar
        print('[ ]mover esquerda\n[2]mover direita')
    elif player.x == 1:#segundo  quarto do andar
        print('[1]mover esquerda\n[2]mover direita')
    else:              #terceiro quarto do andar
        print('[1]mover esquerda\n[ ]mover direita')
    if andarPlayer[player.x] == 1: #andar com escada
        print('[3]próximo andar')

    #input
    while gameRunning:
        resposta = str(input('input: '))
        if resposta == '1':  #mover esquerda
            player.x -= 1
            if player.x < 0:
                print('movimento invalido')
                player.x = 0
                continue
        elif resposta == '2':#mover direita
            player.x += 1
            if player.x > 2:
                print('movimento invalido')
                player.x = 2
                continue
        elif resposta == '3':#mover próximo andar
            if quartoPlayer == 1:
                player.y += 1
            else:
                print('movimento invalido')
                continue
        else:
            print('input invalido')
            continue
        break
    
    #break