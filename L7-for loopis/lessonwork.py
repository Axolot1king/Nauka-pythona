from random import randint

trays = 1
liczba = randint(1, 1000)

for x in range(10):
    y = int(input('enter number:'))

    if y == liczba:
        print('doog')
        break

    elif y < liczba:
        print('More MOREEEEEEEE')

    else:
        print('too much cool down')

    if x == 9:
        print('you failed the trays are too much')
        print('Hosed number is: ' + str(liczba))

    print("it's your: " + str(trays) + ' try')
    trays += 1