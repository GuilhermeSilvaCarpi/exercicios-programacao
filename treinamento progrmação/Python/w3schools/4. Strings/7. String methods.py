# Todos os metodos de strings retornam strings novas, não alteram as strigs as quais os metodos estão relacionados
texto: str = '   TesTo de TesTes  '

print(texto)
print(texto.capitalize())
print(texto.casefold())
print(texto.center(30))
print(texto.count('T'))
print(texto.endswith('s'))
print(texto.find('tesT'))
print(texto.index('de'))
print(texto.replace('de','DE'))
print(texto.title())
