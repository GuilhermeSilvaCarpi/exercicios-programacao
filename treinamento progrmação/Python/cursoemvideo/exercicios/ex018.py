#aula 08
from math import sin, cos, tan, radians
angulo = float(input('um ângulo '))
angRad = radians(angulo)
print('seno de {:.2f}:     {:.2f}'.format(angulo,sin(angRad)))
print('cosseno de {:.2f}:  {:.2f}'.format(angulo,cos(angRad)))
print('tangente de {:.2f}: {:.2f}'.format(angulo,tan(angRad)))
