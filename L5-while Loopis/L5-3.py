user1Log = 'makaron'
user1Pas = 'ser'
user2Log = 'klopsy'
user2Pas = 'sos'
user3Log = 'chleb'
user3Pas = 'masło'
x = 0

print('Witaj zaloguj się do systemu gotuj nami!')

while x <= 2:
    log = input('Wpisz login: ')
    pas = input('Wpisz hasło: ')

    x += 1

    if log == user1Log and pas == user1Pas or log == user2Log and pas == user2Pas or log == user3Log and pas == user3Pas:
        print(f'Drogi {user1Log} zostałeś zalogowany!')
        x = 0
        break
    elif log == user1Log or log == user2Log or log == user3Log:
        print('Użytkownik istnieje lecz hasło zostało nie poprawnie'
              '\nwpisane')

    else:
        print('Hasło lub login nie poprawne!')


if x > 2:
    print('Konto zablokowane!')