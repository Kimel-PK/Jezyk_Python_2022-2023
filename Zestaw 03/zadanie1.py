import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
	data = json.load(read_file)

linie = {}
obsługiwanePrzystanki = {}

for linia in data['linia'] :
	linie[linia['name']] = []
	if 'przystanek' in linia :
		for przystanek in linia['przystanek'] :
			linie[linia['name']].append (przystanek['name'][:-3])
			obsługiwanePrzystanki[przystanek['name'][:-3]] = True
		
with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(linie, file, ensure_ascii=False)


print ("Numer linii -> liczba przystanków")
print ()
for linia in sorted(linie, key=lambda k: len(linie[k]), reverse=True):
    print (linia + " -> " + str (len (linie[linia])))


print ()
print ()
print ("Obsługiwane przystanki:")
print ()
for przystanek in obsługiwanePrzystanki :
	print (przystanek)