
nome = str(input('um nome: ')).strip().title()

print('bom dia {}!!'.format(nome))

if 'Gustavo' in nome:
    print('belo nome')
elif 'Guilherme' in nome:
    print('nome legal')
else:
    print(':)')
