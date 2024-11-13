# Eingabe der IP-Adresse und Subnetzmaske
firstoctett = input("Bitte gebe das erste Oktett der IP-Adresse an: ")
secondoctett = input("Bitte gebe das zweite Oktett der IP-Adresse an: ")
thirdoctett = input("Bitte gebe das dritte Oktett der IP-Adresse an: ")
fourthoctett = input("Bitte gebe das vierte Oktett der IP-Adresse an: ")
subnetmask = int(input("Bitte gebe die Subnetzmaske an (CIDR-Notation, z.B. 29): "))

# Zusammenstellung der IP-Adresse in einer Liste
ip_adress_complete = [firstoctett, secondoctett, thirdoctett, fourthoctett]

# Umwandlung der IP-Adresse in Binärform
ip_binaer = ''.join([format(int(octet), '08b') for octet in ip_adress_complete])

# Umwandlung der Subnetzmaske in Binärform
bits = subnetmask
subnetmask_bin = '1' * bits + '0' * (32 - bits)

# Aufteilung in Oktette der Subnetzmaske
subnetmask_binaer_octett = '.'.join([subnetmask_bin[i:i+8] for i in range(0, 32, 8)])

# Netzadresse in Binärform berechnen
netzadresse_binaer = ''.join([format(int(ip_binaer[i:i+8], 2) & int(subnetmask_bin[i:i+8], 2), '08b') for i in range(0, 32, 8)])

# Broadcast-Adresse in Binärform berechnen
broadcast_binaer = ''.join([format(int(ip_binaer[i:i+8], 2) | int(''.join(['1' if bit == '0' else '0' for bit in subnetmask_bin[i:i+8]]), 2), '08b') for i in range(0, 32, 8)])

# Umwandlung der Netzadresse und Broadcast-Adresse in Dezimalform
netzadresse = '.'.join([str(int(netzadresse_binaer[i:i+8], 2)) for i in range(0, 32, 8)])
broadcast = '.'.join([str(int(broadcast_binaer[i:i+8], 2)) for i in range(0, 32, 8)])

print(f"Netzadresse: {netzadresse}")
print(f"Broadcast-Adresse: {broadcast}")