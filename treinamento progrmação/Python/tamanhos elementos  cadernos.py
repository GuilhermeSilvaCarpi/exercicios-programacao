"""folhaA4 = [21.0, 29.7]
#preco material
#preco unidade de material = preco / quantidade
precos = {'folha'     : 16   / 500,
          'm²Papelao' : 10.4 / (100*80),
          'm²Napa'    : 9.5  / (150*50)}

#tamanhos elementos  cadernos 
def calculandoDimensoes(x,y):
    return {'folha' : [x, y],
            'capa'  : [x+0.5, y+1],
            'fundo' : [1.5 if x>10.5 else 1, y+1],
            'napa'  : [(x+0.5) * 2              # capa x * 2
                       + (1.5 if x>10.5 else 1) # fundo x
                       + 1                      # distância entre fundo e capa
                       + (2*2)                  # 2 * sobra de napa pra acabamento
                       ,(y + 1) + (2 * 2)]}# (capa y) + (2 * sobra de napa pra acabamento)
#preco elementos cadernos"""
def calculoPrecos(caderno, folhas, tamanhoFolha):
    return {'folhas' : precos('folha')    * (1),
            'papelao': precos('m²Papelao')* (1),
            'napa'   : precos('m²Napa')   * (caderno('napa')[0]*caderno('napa')[1])}
"""
#variaveis
cadernos = [calculandoDimensoes(15, 21),
            calculandoDimensoes(10.5, 15),
            calculandoDimensoes(7.5, 10.5)]

#outputs
for caderno in cadernos:
    for item in caderno:
        print('{:5}: {}'.format(item, caderno[item]))
    print('-'*20)
    
print('*'*20)
"""
print('-'*20)
print(calculoPrecos(cadernos[0],100,1/2))
print(calculoPrecos(cadernos[1], 70,1/4))
print(calculoPrecos(cadernos[2], 70,1/8))
