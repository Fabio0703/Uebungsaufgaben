year = int(input("Welches Jahr?: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ("Das ist ein Schaltjahr!")
else:
    print("Das ist kein Schaltjahr!")