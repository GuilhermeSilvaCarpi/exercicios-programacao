#aula 7
altura_parede = float(input ('Altura de uma parede: '))
largura_parede = float(input ('Largura de uma parde: '))
parede_m_cubicos = altura_parede * largura_parede
print ('1 lito de tinta para cada 2m²')
print ('"são necessários {} litros de tinta para pintar {}m² de parede"'
	     .format(parede_m_cubicos/2,parede_m_cubicos))
