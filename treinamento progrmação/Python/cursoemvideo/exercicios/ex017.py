#aula 08
'''from math import sqrt

cato = float(input('cateto oposto    '))
cata = float(input('cateto adjacente '))
hipotenusa = sqrt(cata**2 + cato**2)
print('a hipotenusa dos catetos {} e {} é {:.2f}'
	.format(cata, cato, hipotenusa))'''

from math import hypot

catOp = float(input('cateto oposto    '))
catAd = float(input('cateto adjacente '))
hipotenusa = hypot(catOp, catAd)
print('a hipotenusa dos catetos {} e {} é {:.2f}'.format(catOp,catAd, hipotenusa))