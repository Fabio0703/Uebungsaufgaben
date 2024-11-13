def spielerregistrierung():
    spieler = []
    for i in range(2):
        while True:
            name = input(f"Gib den Namen für Spieler {i + 1} ein (3-15 Zeichen): ")
            if 3 <= len(name) <= 15:
                spieler.append(name)
                break
            print("Ungültiger Name. Bitte erneut eingeben.")
    return spieler


def initialisiere_spielfeld():
    return [[' ' for _ in range(7)] for _ in range(6)]


def drucke_spielfeld(spielfeld):
    for reihe in spielfeld:
        print('|'.join(reihe))
        print('-' * 13)


def mache_zug(spielfeld, spalte, spieler_zeichen):
    for reihe in reversed(spielfeld):
        if reihe[spalte] == ' ':
            reihe[spalte] = spieler_zeichen
            return


def pruefe_gewinn(spielfeld, spieler_zeichen):
    for reihe in spielfeld:
        for i in range(4):
            if reihe[i:i + 4] == [spieler_zeichen] * 4:
                return True
    for spalte in range(7):
        for reihe in range(3):
            if all(spielfeld[reihe + i][spalte] == spieler_zeichen for i in range(4)):
                return True
    for reihe in range(3):
        for spalte in range(4):
            if all(spielfeld[reihe + i][spalte + i] == spieler_zeichen for i in range(4)) or \
                    all(spielfeld[reihe + i][spalte + 3 - i] == spieler_zeichen for i in range(4)):
                return True
    return False


def vier_gewinnt():
    spieler = spielerregistrierung()
    spielfeld = initialisiere_spielfeld()
    spieler_zeichen = ['X', 'O']
    aktueller_spieler = 0

    while True:
        drucke_spielfeld(spielfeld)
        while True:
            try:
                spalte = int(input(f"{spieler[aktueller_spieler]}, wähle eine Spalte (1-7): ")) - 1
                if 0 <= spalte < 7 and spielfeld[0][spalte] == ' ':
                    break
                print("Ungültiger Zug. Bitte erneut versuchen.")
            except ValueError:
                print("Bitte eine Zahl zwischen 1 und 7 eingeben.")

        mache_zug(spielfeld, spalte, spieler_zeichen[aktueller_spieler])

        if pruefe_gewinn(spielfeld, spieler_zeichen[aktueller_spieler]):
            drucke_spielfeld(spielfeld)
            print(f"Herzlichen Glückwunsch, {spieler[aktueller_spieler]}! Du hast gewonnen!")
            break

        aktueller_spieler = 1 - aktueller_spieler


if __name__ == "__main__":
    vier_gewinnt()
