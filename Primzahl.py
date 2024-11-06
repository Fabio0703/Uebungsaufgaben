zahl = int(input("Zahl zum Überprüfen: "))

if zahl > 1:
    for i in range(2, zahl):
        if zahl % i == 0:
            print(f"{zahl} ist keine Primzahl.")
            break
    else:
        print (f"{zahl} ist eine Primzahl.")
else:
    print (f"{zahl} ist keine Primzahl.")