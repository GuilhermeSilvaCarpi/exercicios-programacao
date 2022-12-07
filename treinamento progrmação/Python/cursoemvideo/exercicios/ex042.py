# aula 12
# inputs
triang = [float(input('Primeiro seguimento: ')),
          float(input('Segundo  seguimento: ')),
          float(input('Terceiro seguimento: '))
          ]
# outputs
## se pode ser triangulo
if (triang[0] + triang[1] > triang[2]
and triang[1] + triang[2] > triang[0]
and triang[2] + triang[0] > triang[1]):
    print('O triângulo de lados {}, {} e {} é:'.format(triang[0], triang[1], triang[2]))
    ## qual tipo de triangulo
    if triang[0] == triang[1] == triang[2]:
        print('EQUILATERO')
    elif (triang[0] == triang[1]
       or triang[1] == triang[2]
       or triang[2] == triang[0]):
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Um triangulo com os lados {}, {} e {} é matematicamente impossivel'.format(triang[0], triang[1], triang[2]))
