# aula 13
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')

inverso = frase[::-1]
"""inverso = ''
print('O inverso de\033[36m {}\033[m é \033[36m'.format(frase), end='')
for letra in range(len(frase) - 1, -1, -1):
    print(frase[letra], end='')
    inverso += frase[letra]
print('\033[m')"""

if inverso == frase:
    print('A frase\033[32m é um palindromo\033[m')
else:
    print('A frase\033[31m não é um palindromo\033[m')
