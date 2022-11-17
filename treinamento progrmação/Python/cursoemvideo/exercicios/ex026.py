#aula 09
string = str(input('digitação de uma string: ')).strip().upper()
print('a letra "a" aparece {} vezes em {}'.format(string.count('A'),string))
print('a primeira letra "a" de {} está em: {}'.format(string,string.find('A')+1))
print('a ultima letra "a" de {} está em:   {}'.format(string,string.rfind('A')+1))
