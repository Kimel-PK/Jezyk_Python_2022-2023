text = input()

uppercase = []
lowercase = []
even = []
odd = []

for char in text :
    if char.isupper () :
        uppercase.append(char)
    elif char.islower () :
        lowercase.append(char)
    elif char.isdigit () :
        if int(char) % 2 == 0 :
            even.append(char)
        else :
            odd.append(char)

uppercase.sort()
lowercase.sort()
even.sort()
odd.sort()

print (''.join (lowercase), ''.join (uppercase), ''.join (odd), ''.join(even), sep='')
