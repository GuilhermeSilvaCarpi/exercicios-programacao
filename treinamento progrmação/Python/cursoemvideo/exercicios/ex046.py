# aula 13
from time import sleep

print('Contagem regressiva:')
for i in range(10, -1, -1):
    sleep(1)
    print(i, end='. ')
else:
    print()
print('Contagem terminada')
print('*estouro de fogos de artifício*')
