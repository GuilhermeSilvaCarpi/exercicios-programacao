#aula 09

nome = str(input('um nome completo: ')).strip()
print('"nome" com letras maiusculas:',nome.upper())
print('"nome" com letras minusculas:',nome.lower())
print('quantas letras "nome" tem?  :',len(nome.replace(' ','')))
#print('quantas letras "nome" tem?  :',(len(nome) - nome.count(' ')))

#print('"primeiro" nome de "nome" tem {} letras'.format(nome.find(' ')))
print('"primeiro" nome de "nome" tem {} letras'.format(len(nome.split()[0])))
