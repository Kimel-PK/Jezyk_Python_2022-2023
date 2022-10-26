najgłębszyPoziom = 0
najgłębszeListy = []

def zagnieźdź (lista) :
	
	global najgłębszyPoziom
	global najgłębszeListy
	
	najgłębszyPoziom = 0
	najgłębszeListy = []
	
	szukaj (lista, 0)
	
	for i in najgłębszeListy :
		i.append (i[len(i) - 1] + 1)
	
	return lista

def szukaj (lista, poziom) :
	
	global najgłębszyPoziom
	global najgłębszeListy
	
	for i in lista :
		if isinstance (i, list)	:
			szukaj (i, poziom + 1)
	
	if poziom > najgłębszyPoziom :
		najgłębszyPoziom = poziom
		najgłębszeListy = []
		najgłębszeListy.append (lista)
	elif poziom == najgłębszyPoziom :
		najgłębszeListy.append (lista)

lista = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
print (str (lista) + " => " +  str (zagnieźdź (lista)), end='\n\n')
lista = [1, [2, 3], 4]
print (str (lista) + " => " +  str (zagnieźdź (lista)), end='\n\n')
lista = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
print (str (lista) + " => " +  str (zagnieźdź (lista)), end='\n\n')
lista = [1, [3], [2]]
print (str (lista) + " => " +  str (zagnieźdź (lista)), end='\n\n')