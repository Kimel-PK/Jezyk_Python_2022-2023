# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo (self, x) :
        print ("wykonanie foo(" + str (self) + ", " + str (x) + ")")
    
    @classmethod
    def class_foo (self, x) :
        print ("class_foo(" + str (self) + ", " + str (x) + ")")
    
    @staticmethod
    def static_foo (x) :
        print ("wykonanie static_foo(" + str (x) + ")")

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Zwierze (ABC) :
    @abstractmethod
    def dajGłos (self) :
        pass

class Kaczka (Zwierze) :
    def dajGłos(self):
        print ("Kaczka robi kwa kwa")

class Pies (Zwierze) :
    def dajGłos(self):
        print ("Pies robi hau hau")

k = Kaczka ()
k.dajGłos ()
p = Pies ()
p.dajGłos ()

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

print ("\n\n\n")

class Termometr :
    def __init__ (self) :
        self.min = float('inf')
        self.max = float('-inf')
        self._temperatura = 0
    
    @property
    def temperatura (self) :
        print ("======== Termometr ========")
        print ("Max: " + str (self.max))
        print ("Min: " + str (self.min))
        print ("Ostatni pomiar: ", end="")
        return self._temperatura
    
    @temperatura.setter
    def temperatura (self, temperatura) :
        print ("Zarejestrowano temperature " + str (temperatura))
        if temperatura > self.max :
            self.max = temperatura
            print ("Zarejestrowano nową najwyższą temperaturę !")
        if temperatura < self.min :
            self.min = temperatura
            print ("Zarejestrowano nową najniższą temperaturę !")
        
        self._temperatura = temperatura

t = Termometr ()
t.temperatura = 5
t.temperatura = 3
t.temperatura = 2
t.temperatura = 4
t.temperatura = 3
t.temperatura = -2
t.temperatura = 3
t.temperatura = 13
t.temperatura = 5

print (t.temperatura)