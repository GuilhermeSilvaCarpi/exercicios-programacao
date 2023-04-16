#iniciando
participantes = [
'Ana', 'Mario', 'João', 'José', 'Maria',
'Joana', 'Josele', 'Anio', 'Amanda', 'Armando'
]
print('Lista de participantes:', participantes)

# desclassificando
print('-'*50)
desclassificados = ['João', 'Anio', 'Joana']
for  desc in desclassificados:
    participantes.remove(desc)
print('Foram desclassificados:', desclassificados)
print('Restaram', participantes)

# podio
print('-'*50)
print('Pódio:', participantes[:3])
