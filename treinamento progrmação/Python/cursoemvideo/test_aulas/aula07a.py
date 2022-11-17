print('='*40)
print('|{:^38}|'.format('aula07'))
print('='*40)
nome = input('Digitar nome: ')
print('um prazer conhecer {:-<20}!'.format(nome))
print('um prazer conhecer {:-^20}!'.format(nome))
print('um prazer conhecer {:->20}!'.format(nome))
print()

print('='*40)
n1 = int(input('Um numero: '))
n2 = int(input('Um numero: '))
s  = n1 +  n2
m  = n1 *  n2
d  = n1 /  n2
di = n1 // n2
e  = n1 ** n2
print('-'*40)
print('{:^5} + {:^5} = {:^5}'.format(str(n1),str(n2),str(s)))
print('{} x {} = {}'.format(n1,n1,m))
print('{} % {} = {:.3f}'.format(n1,n2,d))
print('{} // {} = {}'.format(n1,n2,di))
print('{} ** {} = {}'.format(n1,n2,e))
print('='*40)
print('isso aqui é uma cola de linha do python',end=' # ')
print('...')
print('isso aqui é uma \n quebra de linha do python')
