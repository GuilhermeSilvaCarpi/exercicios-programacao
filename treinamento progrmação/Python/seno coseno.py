from math import sin, cos, radians
print('-'*21)
hipotenusa = float(input('uma hipotenusa '))
angulo     = float(input('um angulo      '))

catOposto    = hipotenusa * sin(radians(angulo))
catAdjacente = hipotenusa * cos(radians(angulo))
print('')
print('cateto oposto    {:.2f}'.format(catOposto))
print('cateto adjacente {:.2f}'.format(catAdjacente))
print('')
print('y {:.2f}'.format(catAdjacente))
print('x {:.2f}'.format(catOposto))
print('-'*21)
