# aula 12
from datetime import date

# inputs
anonasc = int(input('Ano de  nascimento: '))
anoatual = int(date.today().year)
idade = anoatual - anonasc

maioridade = 18
# outputs
print('Quem nasceu em {} tem/terá {} anos em {}.'.format(anonasc, idade, anoatual,))
if idade < maioridade:
    print('Ainda faltam {} anos para poder ocorrer o alistamento'.format(maioridade - idade))
    print('O alistamento poderá ser em {}'.format(anoatual + (maioridade - idade)))
elif idade == 18:
    print('Quem tem {} anos deve se alistar IMEDIATAMENTE'.format(idade))
else:
    print('Quem tem {} anos já deveria ter se alistado a {} anos'.format(idade, (anoatual - anonasc - 18)))
    print('O alistamento foi ou deveria ter sido em {}'.format(anonasc + 18))
