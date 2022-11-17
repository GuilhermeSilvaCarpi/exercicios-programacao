n1 = float(input('uma nota:   '))
n2 = float(input('outra nota: '))
media = (n1 + n2)/2
print('media {:.1f}'.format(media),'aprovada'if media >= 7 else'reprovada')
