v = float(input('Digite a velocidade do carro'))
if v > 80:
    print('O carro foi multado')
    m = (v-80) * 7
    print('A multa vai custar R${:.2f}'.format(m))
else:
    print('O carro esta dentro da velocidade')
