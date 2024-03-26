"""
def Drukowanie_pion():
    ort = 'ortografia'
    n = len(ort)
    x = 0
    while x < n:
        print(ort[x])
        x += 1
"""

def Drukowanie_pion(userWord, userNumber = 1):
    for y in range(userNumber):
        for x in range(len(userWord)):
            print(userWord[x])
        if y != userNumber -1:
            print()


user_word = input('Enter word: ')
user_number = input('enter number words gonna be '
                    '\nprinted: ')
if user_number == '':
    Drukowanie_pion(user_word)
else:
    user_number = int(user_number)
    Drukowanie_pion(user_word, user_number)