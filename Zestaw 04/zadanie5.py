from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    # zdefiniuj __init__ i argumenty x, y
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    # __init__ i jeden argument x, wołanie __init__ bazowego
    def __init__(self, x) :
        super().__init__(x, x)

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
# zdefiniuj pole, zwróć x*y z instancji
def pole (self) :
    return self.x * self.y

@dispatch(Prostokat, int, int)
# funkcja pole, najpierw przypisz argumenty do x, y instancji, potem policz pole powierzchni
def pole (self, x, y) :
    self.x = x
    self.y = y
    return x * y

@dispatch(Kwadrat)
# funkcja pole
def pole (self) :
    return self.x * self.x

@dispatch(Kwadrat, int)
# funkcja pole z podanym argumentem boku
def pole (self, x) :
    self.x = x
    return x * x

# testy

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)

def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i)) # polymorphism at runtime

polaPowierzchni([a,b,c])