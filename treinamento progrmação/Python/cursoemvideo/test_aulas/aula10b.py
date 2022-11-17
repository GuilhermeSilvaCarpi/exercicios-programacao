nome = str(input('um nome: ')).strip()
if nome.split()[0].capitalize() == 'Guilherme':
    print('Guilherme')
else:
    print('um nome que não é Guilherme')
print('bom dia, {}'.format(nome.capitalize()))
