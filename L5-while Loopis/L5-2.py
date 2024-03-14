#TODO zrobić notatki i sforkować zadanie

from random import randint

x = 0
trays = 1
liczba = randint(1, 100)

while x != liczba:

    x = int(input('write number you think i chose in range 1-100:'))
    if x == liczba:
        print('Good')
        print("you have", trays, "trays")
    else:
        trays += 1

    if x < liczba:
        print("number must be bigger!")
    if x > liczba:
        print("number must be smaller!")