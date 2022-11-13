def odwracanie (L, left, right) :
	
	left = int (left)
	right = int (right)
	
	i = 0
	połowa = (right - left) // 2
	while(i <= połowa):
		
		temp = L[left]
		L[left] = L[right]
		L[right] = temp
		
		left += 1
		right -= 1
		i += 1

def odwracanie_rek(L, left, right) :
	
	if left >= right:
		return
	
	left = int (left)
	right = int (right)
	
	temp = L[left]
	L[left] = L[right]
	L[right] = temp
	
	odwracanie_rek(L, left + 1, right - 1)

print ("Podaj elementy tablicy, symbol '-' kończy dodawanie")

L = []

while True :
	odczytany = input ('?> ')
	if odczytany == '-' :
		break
	L.append (odczytany)

print ("Wczytana lista:")
print (L)

left = input ("Podaj element początkowy: ")
right = input ("Podaj element końcowy: ")

print ("Odwrócona lista:")
odwracanie (L, left, right)
print(L)

print ("Odwrócona lista z użyciem rekurencji:")
odwracanie_rek(L, left, right)
odwracanie_rek(L, left, right)
print(L)