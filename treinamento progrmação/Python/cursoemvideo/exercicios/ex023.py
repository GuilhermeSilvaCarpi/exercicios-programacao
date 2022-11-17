#aula 09
n = int(input('um número entre 0 e 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

'''n2 = int(n) 
#milhar
m = n2//1000
n2 = n2 - (m*1000)
#centena
c = n2//100
n2 = n2 - (c*100)
#dezena
d = n2//10
n2 = n2 - (d*10)
#unidade
u = n2//1'''

print('unidade: ',u)
print('dezena:  ',d)
print('centena: ',c)
print('milhar:  ',m)

'''num = str(n)
num = num.strip()
num = '0000' + num
print('unidade: ',num[-1])
print('dezena:  ',num[-2])
print('centena: ',num[-3])
print('milhar:  ',num[-4])'''

