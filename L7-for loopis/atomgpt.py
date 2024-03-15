
import os
# Console cleaning
os.system('cls')

from time import sleep
sleep(1)

code = input("Enter the 4-digit code to arm the bomb: ")

if code == "3254":
    print("Bomb armed successfully. Countdown initiated.")

    for i in range(15, -1, -1):
        print("Time left:", i, "seconds")
        sleep(1)

    print("Boom! The bomb exploded!")
else:
    print("Incorrect code. Bomb not armed.")