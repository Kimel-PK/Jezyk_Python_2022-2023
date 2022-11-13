import re

def Konwertuj (liczba) :
	
	if liczba.isdigit() :
		
		liczba = int (liczba)
		if liczba > 3999 :
			return "Błąd! Liczba nie mieści się w zakresie 1-3999!"
		
		return ArabskieNaRzymskie (liczba)
	else :
		if SprawdźPoprawnośćLiczbyRzymskiej (liczba) :
			return RzymskieNaArabskie (liczba)
	
	return "Błąd! Niepoprawna liczba!"
	
def ArabskieNaRzymskie (liczba) :
	
	liczby_arabskie = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
	
	if liczba == 0 :
		return ''
	else :
		for arabska in liczby_arabskie :
			if liczba >= arabska :
				return liczby_arabskie[arabska] + str (ArabskieNaRzymskie (liczba - arabska))
	
	return ''

def SprawdźPoprawnośćLiczbyRzymskiej (liczba):
	return bool (re.search (r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", liczba))

def RzymskieNaArabskie (liczba) :
	
    liczby_rzymskie = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    wynik = 0
	
    for i in range (0, len(liczba)):
        if (i + 1) < len(liczba) and liczby_rzymskie[liczba[i]] < liczby_rzymskie[liczba[i + 1]]:
            wynik -= liczby_rzymskie[liczba[i]]
        else:
            wynik += liczby_rzymskie[liczba[i]]
	
    return wynik

while True :
	print (Konwertuj (input ("?> ")))