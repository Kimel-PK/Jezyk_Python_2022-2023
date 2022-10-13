długość = int (input("Podaj długość miarki: "))

miarkaGóra = "|"
miarkaDół = "0"

for x in range (1, długość + 1) :
	
	miarkaGóra += "....|"
	miarkaDół += str (x).rjust (5)
	
miarka = miarkaGóra + "\n" + miarkaDół

print (miarka)