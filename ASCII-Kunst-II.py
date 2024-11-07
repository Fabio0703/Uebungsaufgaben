size = int(input("Gib eine Zahl ein, die größer als 0 ist: "))

#Oberer Teil der Sanduhr
for i in range(size, 0, -1):
    print('*' * i)

# Leerzeile zwischen den beiden Teilen
print()

# Unterer Teil der Sanduhr
for i in range(1, size + 1):
    print('*' * i)