import math

inp = input().split()
k = int (inp[0])
m = int (inp[1])

matrix = []

for i in range (0, k) :
    matrix.append(input().split()[1:])

for y in range (0, len(matrix)) :
    for x in range (0, len(matrix[y])) :
        matrix[y][x] = int(matrix[y][x])**2

while len (matrix) > 1 :
    new_row = []
    for a in matrix[0] :
        for b in matrix[1] :
            new_row.append (int(a) + int(b))
    matrix[0] = new_row
    del matrix[1]

max = -math.inf
for x in matrix[0] :
    result = x % m
    if result > max :
        max = result
        
print (max)