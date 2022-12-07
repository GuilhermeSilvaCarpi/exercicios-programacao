#aula 12
# inputs
nota1 = float(input('Digite uma nota  : '))
nota2 = float(input('Digite outra nota: '))

media = (nota1 + nota2) / 2

# outputs
print('tirando {} e {} a média é {:.2f}'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO')
elif media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVAVDO')
