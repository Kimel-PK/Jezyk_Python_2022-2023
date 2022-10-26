x = int (input ("x = "))
y = int (input ("y = "))
z = int (input ("z = "))
n = int (input ("n = "))

print ([[i, j, k] for i in range (x + 1) for j in range (y + 1) for k in range (z + 1) if i + j + k != n])