zahl = int(input("Zahl zum Überprüfen: "))
primfaktoren = []
kleinster_teiler = 2 # kleinster Primfaktor

while kleinster_teiler * kleinster_teiler <= zahl: #zur Zerlegung in Primfaktoren, müssen nur Teiler bis zur Quadratwurzel von der zu überprüfenden Zahl gefunden werden. Bei bspw. 60 also bis 7, da Wurzel 7,75 ergibt.
    if zahl % kleinster_teiler == 0:
        primfaktoren.append(kleinster_teiler)
        zahl = zahl // kleinster_teiler
    else:
        kleinster_teiler += 1

if zahl > 1:
    primfaktoren.append(zahl)

print("Die Primfaktoren lauten:", primfaktoren)
