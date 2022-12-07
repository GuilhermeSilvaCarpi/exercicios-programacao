# aula 12
# inputs
peso   = float(input('massa(Kg): '))
altura = float(input('altura (em m): '))
imc = peso / altura **2
# outputs
print('-'*21)
print('O IMC dessa deu: {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')
