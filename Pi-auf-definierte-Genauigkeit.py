anzahl_iterationen = int(input("Bitte gib die Anzahl der Iterationen ein: "))

pi_approx = 0
for i in range(anzahl_iterationen):
    pi_approx += ((-1) ** i) / (2 * i + 1)

pi_wert = 4 * pi_approx

print(f"Die angenäherte Zahl Pi nach {anzahl_iterationen} Iterationen ist: {pi_wert}")
