import random

bits = int(input("Bitte gebe die Zahlengröße in Bits an: "))
max_num = (1<<bits)-1

randomnumber= random.randint(0, max_num)

while True:
    guess = int(input(f"Bitte eine Zahl im Bereich zwischen 0 und {max_num} angeben: "))
    if guess < randomnumber:
        print ("Die gesuchte Zahl ist größer!")
    elif guess > randomnumber:
        print ("Die gesuchte Zahl ist kleiner!")
    else:
        print ("Super!")
        break


