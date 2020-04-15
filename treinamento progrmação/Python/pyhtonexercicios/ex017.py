"""a = float(input('cateto oposto'))
b = float(input('cateto adjasente'))
c = (a ** 2 + b ** 2) ** (1/2)
print('A hipotenusa é igual a {:.2f}'.format(c))"""

from math import hypot

a = float(input('cateto oposto'))
b = float(input('cateto adjasente'))
c = hypot(a, b)
print('A hipotenusa é igual a {:.2f}'.format(c))
