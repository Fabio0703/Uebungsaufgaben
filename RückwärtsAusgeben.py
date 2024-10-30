number = input("Eingabe von beliebig vielen Zahlen, getrennt durch ein Leerzeichen:")
number_list = number.split()
for wert in reversed(number_list):
    print (wert[::-1], end=" ")