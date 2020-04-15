v = float(input('Qual a distância da viagem? km'))
if v < 201:
    vm = v * 0.50
    print('A viagem custou R${:.2f}'.format(vm))
else:
    vm = v * 0.45
    print('A viagem custou R${:.2f}'.format(vm))
