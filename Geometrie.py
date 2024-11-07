#a) Flächenberechnung eines Kreises
from math import pi
radius = int(input("Gib Zahl ein, die größer als 0 ist: "))
pi = pi
qm = (radius**2)*pi
print ("Die Fläche beträgt: ", qm)

#b) Flächenberchnung eines Rechtecks

length = int(input("Gib eine Ganzzahl ein, die größer als 0 ist: "))
width = int(input("Gib eine zweite Ganzzahl ein, die größer als 0 ist: "))
sqm = length * width
print ("Die Fläche betrögt: ", sqm)