#aula 10
d = int(input('distância de uma viagem em km: '))
passagem = 0.0

'''if d <= 200:
    passagem = 0.5 * d
else:
    passagem = 0.45 * d'''

passagem = 0.5 * d if d <= 200  else 0.45 * d

print('a hipotética passagem vai custar: R${:.2f}'.format(passagem))
