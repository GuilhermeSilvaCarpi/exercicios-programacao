from math import radians, sin, cos, tan

ang = float(input('Digite o angulo que você deseja'))
a = radians(ang)
sen = sin(a)
csen = cos(a)
tan = tan(a)
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o cosseno de{:.2f}'.format(ang, csen))
print('O ângulo de {} tem a tanjente de {:.2f}'.format(ang, tan))
