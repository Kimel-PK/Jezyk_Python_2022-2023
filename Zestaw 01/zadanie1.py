szerokość = int (input ("Podaj szerokość podstawy: "))

if szerokość % 2 == 0 :
	szerokość -= 1

print ("\n" + "*" * szerokość)

for x in range(1, szerokość // 2, 1) :
	print (" " * x + "*", end = "")
	print (" " * (szerokość - x * 2 - 2), end = "")
	print ("*")
	
print (" " * (szerokość // 2) + "*\n")