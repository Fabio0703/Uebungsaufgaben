divisor = int(input("Welcher Divisor soll geprüft werden?: "))
max = int(input("Bis zu welcher Zahl?: "))

for i in range(max+1):
    if i % divisor == 0 and i <= max:
        print(i)