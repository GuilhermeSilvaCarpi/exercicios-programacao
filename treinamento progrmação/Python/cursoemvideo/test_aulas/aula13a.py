# For com alcance de 5 a 10.
for i in range(5,11):
    print(i,end=' ')
print('')

cadeia = [[ 0, 1, 2, 3, 4],
          [ 5, 6, 7, 8, 9],
          [10,11,12,13,14],
          [15,16,17,18,19],
          [20,21,22,23,24]]
# For aninhado com if.
for item in cadeia:
    for subitem in item:
        print('[X]'if subitem % 2 == 0 else '[ ]', end='')
    print('')
# Vídeo
## For com range (intervalo).
for c in range(1,6):
    print('oi')
print('FIM')

## For com range em ordem decrescente.
for c in range(10,1,-1):
    print('{} '.format(c), end='')
print()

## For com range de passo 2 (avançando "pulando" de dois em dois).
for c in range(0,11,2):
    print('[{}] '.format(c), end='')
print()

## Definindo um range com inputs.
i = int(input('inicio: '))
f = int(input('final:  '))
p = int(input('passo:  '))
for c in range(i, f+1, p):
    print('{} '.format(c), end='')
print()

## Imputs dentro de um loop for. 
s = 0
for c in range(0, 3):
    n = int(input('um numero: '))
    s += n
print('A soma entre os 3 numeros é : {}'.format(s))
