#Strings

frase = 'Curso em Vídeo Python'
print(frase)

#analise

#__len(frse)
#__largura
print('largura de frase')
print(len(frase))

#__frase.count
#____contar quantas vezes "o" aparece na "frase"
print('quantas vezes "o" aparece na "frase"')
print(frase.count('o'))

#____contar quantos "o" aparecem de 0 a 12 na em "frase"
print('quantos "o" aparecem de 0 a 12 na em "frase"')
print(frase.count("o",0,13))

#__frase.find()
#____encontrar uma string expecifica dentro de uma string
print('onde "em" é emcontrado em "frase"')
print(frase.find('em'))

#____frase.find(valor não encontrado em frase)
print(frase.find('uou'))

#__"Curso" in frase
#____existe string especifica em frase?
print('Curso' in frase)
