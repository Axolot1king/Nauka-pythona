#TODO zrobić notatki i sforkować zadanie

from random import randint

x = 0
liczba = randint(1,100)

while x != liczba:

    x = int(input('write number you think i chose in range 1-100:'))
    if x == liczba:
        print('Good')