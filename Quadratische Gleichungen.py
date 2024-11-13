value_a = float(input("a: "))
value_b = float(input("b: "))
value_c = float(input("c: "))

diskriminante = value_b**2 - 4*value_a*value_c

if diskriminante > 0:
    print ("Ergebnis: 2")
elif diskriminante == 0:
    print ("Ergebnis: 1")
else:
    print ("Ergebnis: 0")