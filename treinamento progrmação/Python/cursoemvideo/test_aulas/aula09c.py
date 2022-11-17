#Strings

frase = 'Curso em Vídeo Python'
print(frase)

#transformação de strings

#__frase.replace('Python','Android')
#__reposicionar(trocar) 'Python' por 'Android'
print(frase.replace('Python','Android'))

#__frase.upper()
#__string maiuscula
print(frase.upper())

#__frase.lower()
#__letras minusculas
print(frase.lower())

#__frase.capitalize()
#__só primeira letra de uma string maiuscula
print(frase.capitalize())

#__frase.title
#__primeira letra de todas palavras de "frase" em maiusculas
print(frase.title())

#__frase.strip
#__remover espaços no inicio e final de strings

frase2 = '   Curso programação  '
print(frase2.strip())

#____rstrip right(direita) strip
print(frase2.rstrip())

#____lstrip left (esqueda) strip
print(frase2.lstrip())
