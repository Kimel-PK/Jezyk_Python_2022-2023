tekst = input("Wpisz tekst: ")

print ("Ilość słów: " + str (len (tekst.split())))

słownik = {}

litery = 0
cyfry = 0
for x in tekst :
	
	słownik[x] = 0
	
	if x.isalpha() :
		litery += 1
	elif x.isnumeric() :
		cyfry += 1

for x in tekst :
	słownik[x] += 1

print ("Ilość liter: " + str(litery))
print ("Ilość cyfr: " + str(cyfry))
print ()
print ("Statystyki:")
print (słownik)