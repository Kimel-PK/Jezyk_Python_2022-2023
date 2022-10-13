szerokość = int (input ("Podaj szerokość: "))
wysokość = int (input ("Podaj wysokość: "))

prostokąt = "\n+"

for x in range (szerokość) :
	prostokąt += "---+"

for y in range (wysokość) :
	linia1 = "\n|"
	linia2 = "\n+"
	for x in range (szerokość) :
		linia1 += "   |"
		linia2 += "---+"
	prostokąt += linia1 + linia2
	
print (prostokąt + "\n")