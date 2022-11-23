from math import hypot, atan, sin, cos, sqrt

class Zespolona:
	def __init__(self, r, i):
		self.r = r
		self.i = i

	def conjugate(self):
		return self.__class__(self.r, -self.i)

	def argz(self):
		return atan(self.i / self.r)
	
	def __abs__(self):
		Zespolona (sqrt(self.r ** 2 - self.i ** 2), 0)

	def __repr__(self):
		return "Zespolona (" + str (self.r) + ", " + str (self.i) + ")"

	def __str__(self):
		return "(" + str (self.r) + ("+" if self.i > 0 else "") + str (self.i) + "j)"

	def __add__(self, other):
		if isinstance(other, Zespolona) :
			return Zespolona (self.r + other.r, self.i + other.i)
		else :
			return Zespolona (self.r + other, self.i)

	def __sub__(self, other):
		if isinstance(other, Zespolona) :
			return Zespolona (self.r - other.r, self.i - other.i)
		else :
			return Zespolona (self.r - other, self.i)

	def __mul__(self, other):
		if isinstance(other, Zespolona) :
			return Zespolona (self.r * other.r - self.i * other.i, self.i * other.r + self.r * other.i)
		else :
			return Zespolona (self.r * other, self.i * other)

	def __radd__(self, other):
		if isinstance(other, Zespolona) :
			return Zespolona (self.r + other.r, self.i + other.i)
		else :
			return Zespolona (self.r + other, self.i)

	def __rmul__(self, other):
		if isinstance(other, Zespolona) :
			return Zespolona (self.r * other.r, self.i * other.i)
		else :
			return Zespolona (self.r * other, self.i * other)

	def __rsub__(self, other):
		if isinstance(other, Zespolona) :
			return Zespolona (-self.r + other.r, -self.i + other.i)
		else :
			return Zespolona (-self.r + other, -self.i)

	def __eq__(self, other):
		if isinstance(other, Zespolona) :
			return self.r == other.r and self.i == other.i
		else :
			return self.r == other and self.i == 0

	def __ne__(self, other):
		if isinstance(other, Zespolona) :
			return self.r != other.r or self.i != other.i
		else :
			return self.r != other or self.i != 0

	def __pow__(self, other):
		wynik = self
		for _ in range (other - 1) :
			wynik *= self
		return wynik

def main():
	print ("obecny wynik | oczekiwana wartość")
	print ()
	print("Liczby zespolone")
	a = Zespolona(2, 5)
	b = Zespolona(1, -3)
	print(a, "| (2+5j)")
	print(b, "| (1-3j)")
	b_copy = eval(repr(b))
	print(type(b_copy), b_copy.r, b_copy.i, "| <class '__main__.Zespolona'> 1 -3")
	print(a + b, "| (3+2j)")
	print(a - b, "| (1+8j)")
	print(a + 4, "| (6+5j)")
	print(7 - a, "| (5-5j)")
	print(a * 4, "| (8+20j)")
	print(a * (-4), "| (-8-20j)")
	print(a == Zespolona(2, 5), "| True")
	print(a == b, "| False")
	print(a != b, "| True")
	print(a != Zespolona(2, 5), "| False")
	print(a ** 2, "| (-21+20j)")
	print(b ** 4, "| (28+96j)")


if __name__ == "__main__":
	main()