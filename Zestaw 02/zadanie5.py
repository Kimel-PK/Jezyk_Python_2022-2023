def fun(N) :
	
	binarna = bin(N) + "1"
	przerwa = 0
	tmp = 0
	zmaż = False
	
	for i in binarna[2:] :
		
		if i == '0' :
			tmp += 1
		else :
			if tmp > przerwa :
				przerwa = tmp
			tmp = 0
			zmaż = False
	
	return przerwa

print ("Najdłuższa przerwa binarna: " + str (fun (int (input ("Podaj liczbę: ")))))