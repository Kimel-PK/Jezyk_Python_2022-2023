import sys

argv = sys.argv[1:]

for i in range (len (argv)) :
	
	liczba = int (argv[i])
	
	print (str (liczba) + " = ", end = "")
	
	rozkład = ""
	k = 2
	
	while liczba > 1 :
		ilość = 0
		while liczba % k == 0 :
			ilość += 1
			liczba /= k
			
		if (ilość > 0) :
			rozkład += str(k) + "^" + str(ilość) + "*"
		k += 1
			
	print (rozkład[:-3])