'''
Uma variável só está disponível dentro da região (escopo) ao
qual ela é criada.

Uma variável que é feita dentro de uma função geralmente é
utilizável somente dentro dela (o escopo na qual ela foi criada)

É possível haver escopos dentro de escopos. Com isso é possívela
acessar alguma variável do escopo exterior dentro de um escopo
interior.
'''
# Escopo global
'''
Qualquer variável criada sem identação é pertencente ao escopo
global.
Essas variáveis são acessíveis a qualquer escopo interno: em
qualquer função.
'''
# Nomeando variáveis
'''
Quando uma variável dentro de um escopo é criada com o mesmo nome
de uma variável global: o python trata a variável interna como
outra diferente, e toda vez que o nome dela é chamado no escopo
interno não se refere a variável global.
'''
x = 10
def função():
    x = 20
    print('"x" em escopo interno:', x)
função()
print('"x" em escopo global:', x)

# Palavra chamee "global"
'''
Com essa palavra chave é possível criar ou editar uma variável
global dentro de um escopo local.
'''
def função2():
    global y
    y = 5
    global x
    x = 25
função2()
print('"y" em escopo global:', y)
print('"x" em escopo global:', x)
