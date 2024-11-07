while True:
    # Modusauswahl
    modus = input("Möchtest du verschlüsseln oder entschlüsseln? (v/e): ").lower()

    #Verschlüsselungsmodus
    if modus == 'v':
        x = int(input("Gib die Zahl ein, die verschlüsselt werden soll: "))
        passwort = int(input("Gib die Passwortzahl ein: "))
        verschlüsselt = x ^ passwort
        print("Verschlüsselte Zahl:", verschlüsselt)
    #Entschlüsselungsmodus
    elif modus == 'e':
        verschlüsselt = int(input("Gib die verschlüsselte Zahl ein: "))
        passwort = int(input("Gib die Passwortzahl ein: "))
        entschlüsselt = verschlüsselt ^ passwort
        print("Entschlüsselte Zahl:", entschlüsselt)
    else:
        print("Ungültige Eingabe. Bitte 'v' für verschlüsseln oder 'e' für entschlüsseln eingeben.")

    # Abfrage nach weiteren Operationen.
    weiter = input("Möchtest du eine weitere Operation durchführen? (j/n): ").lower()
    if weiter != 'j':
        print("Programm beendet.")
        break
