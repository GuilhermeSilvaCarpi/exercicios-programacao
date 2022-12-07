# aula 12
from datetime import date
# inputs
anonasc = int(input('ano de nascimento de um hipotético nadador: '))
idade = date.today().year - anonasc

# outputs
print('O atleta tem {} anos.'.format(idade))
print('classificação : ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
