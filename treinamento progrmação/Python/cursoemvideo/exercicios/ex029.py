#aula 10
v = float(input('uma velocidade de carro em km/h: '))
if v > 80:
    print('"multa de R${:.2f} para o carro hipotético"'.format(7*(v-80)))
print('tenha um bom dia! dirija com segurança!')
