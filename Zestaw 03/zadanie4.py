import functools

def pamiec(func):
	
	słownik = {}
	
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		
		if args in słownik :
			return słownik[args]
		else :
			wynik = func (*args, **kwargs)
			słownik[args] = wynik
			return wynik
	
	return wrapper
	
@pamiec
def fibonacci(n):
	return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
	
for i in range(100):
	print(fibonacci(i))