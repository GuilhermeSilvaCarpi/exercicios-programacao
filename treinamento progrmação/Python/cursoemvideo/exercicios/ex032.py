#aula 10
from datetime import date

ano = int(input('um ano: '))
if ano == 0:
    ano = date.today().year
print('o ano {}'.format(ano),
      'é bissexto'if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
      else'não é bissexto')
