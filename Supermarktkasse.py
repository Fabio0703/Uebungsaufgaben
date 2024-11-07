produkte = []
preis = 0

while True:
    produkt = input("Geben Sie den Preis des Produkts in Cent ein (oder 0 zum Beenden): ")
    produkt = int(produkt)
    if produkt == 0:
        break
    produkte.append(produkt)
    preis += produkt

preis_euro = preis / 100
print(f"Gesamtbetrag: {preis_euro:.2f}€")

gegeben = int(input("Wie viel Geld hat der Kunde in Cent gegeben? "))
rueckgeld = gegeben - preis

scheine_muenzen = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
rueckgabe = {}

for wert in scheine_muenzen:
    anzahl = int(rueckgeld // wert)
    if anzahl > 0:
        rueckgabe[wert] = anzahl
        rueckgeld -= anzahl * wert

print("Rückgeld:")
for wert, anzahl in rueckgabe.items():
    if wert >= 100:
        print(f"{anzahl} x {wert // 100}€")
    else:
        print(f"{anzahl} x {wert} Cent")
