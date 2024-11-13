meine_liste = [int(element.strip()) for element in input("Gib die jeweiligen Zahlen ein, getrennt durch Kommas: ").split(',')]

x = len(meine_liste)
for i in range(x):
    for j in range(0,x-i-1):
        if meine_liste[j] > meine_liste[j+1]:
            meine_liste[j], meine_liste[j+1] = meine_liste[j+1], meine_liste[j]

print(meine_liste)