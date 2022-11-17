#aula 09
nome = str(input('a complete name: ')).strip()
nomeDividido = nome.split()
print('forname: {}'.format(nomeDividido[0]))
print('family name: {}'.format(nomeDividido[-1]))
