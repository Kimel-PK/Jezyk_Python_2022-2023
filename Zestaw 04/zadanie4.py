from functools import singledispatch, singledispatchmethod
from math import ceil

class Dzielenie:
	@singledispatchmethod
	def podziel(self, arg):
		return "Nieznane przeładowanie"

	@podziel.register (list)
	def _(self, arg):
		wynik = arg[0]
		for i in range (1, len (arg)):
			wynik /= arg[i]
		return wynik

	@podziel.register (tuple)
	def _(self, arg):
		wynik = int (arg[0])
		for i in range (1, len (arg)):
			wynik /= int (arg[i])
		return wynik

	@podziel.register (dict)
	def _(self, arg):
		wynik = {}
		for i in arg:
			wynik[i] = i / arg[i]
		return wynik


dzielenie = Dzielenie()

print (dzielenie.podziel ("tekst"))
print (dzielenie.podziel ([1024, 2, 8, 4, 2]))
print (dzielenie.podziel ({1, 2, 3, 4}))
print (dzielenie.podziel (("600", "2", "3"))) 
print (dzielenie.podziel ({2: 4, 10: 5, 15: 3}))

print("\n----------------\n")

@singledispatch
def pole (arg):
	return "Nieznane przeładowanie"

@pole.register
def _(a:int, b:int):
	return a * b

@pole.register
def _(a:float, b:float):
	return ceil (a) * ceil (b)

@pole.register
def _(a:tuple):
	return int (a[0]) * int (a[1])

print (pole ("pies"))
print (pole (2, 5))
print (pole (19.1, 15.0))
print (pole (("7", "6")))