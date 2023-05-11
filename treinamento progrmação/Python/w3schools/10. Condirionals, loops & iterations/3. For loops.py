variável = 'banana'
print(variável)

# Percorrendo um item iterável.
for x in variável:
    print(x, end='-*')
print()

# Percorrendo outro item iterável.
for x in ['um', 'dois', 'três', 'quatro']:
    print(x)

# Percorrendo um item iterável e usando break, que interrompe o loop.
for x in variável:
    print(x,end='-')
    if x == 'n':
        break
print()

# Usando continue, que pula para o próximo passo do loop.
for x in variável:
    if x == 'a':
        continue
    print(x,end='')
print()

# Usando range com um parâmetro.
for x in range(11):
    print(x, end=' ')
print()

# Usando range com 3 parametros: inicio, final, "pulo" (dois parâmetros declaram somente: inicio e final).
for x in range(10,30,2):
    print(x, end=', ')
print()

# Usando "else" em loop for. O bloco do "else" é executado depois que o loop for termina.
for x in range(8):
    print(x, end=', ')
else: # O bloco de código do "else" não será executado se o loop for terminar com um "break".
    print('fim')
print()

# Loops aninhados, são nada menos que loops dentro de loops.
for x in ['computador', 'carro', 'caderno']:
    for y in ['grande', 'bonito', 'útil']:
        print(x,y)

# Declaração "pass", usada para métodos vazios não terem erros.
for x in range(4):
    pass
