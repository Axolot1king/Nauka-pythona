def procent_składany_z_dopłatami(kwota, procent, lata, doplata, czestotliwosc):
    # Zamiana procentu na ułamek dziesiętny
    r = procent / 100
    # Liczba okresów kapitalizacji w roku
    if czestotliwosc == 'tygodniowo':
        okresy = 52
    elif czestotliwosc == 'miesięcznie':
        okresy = 12
    elif czestotliwosc == 'kwartalnie':
        okresy = 4
    elif czestotliwosc == 'rocznie':
        okresy = 1
    else:
        print("Niepoprawna częstotliwość dopłat.")
        return None

    # Obliczenie wartości przyszłej z dopłatami
    przyszła_wartość = kwota * (1 + r / okresy) ** (lata * okresy)
    for t in range(1, lata * okresy + 1):
        przyszła_wartość += doplata * (1 + r / okresy) ** (lata * okresy - t)

    return przyszła_wartość


# Pobranie danych od użytkownika
kwota = float(input("Podaj kwotę początkową: "))
procent = float(input("Podaj stopę procentową (w %): "))
lata = int(input("Podaj liczbę lat: "))
doplaty = input("Czy chcesz dokonywać regularnych dopłat? (tak/nie): ").lower()

if doplaty == 'tak':
    doplata = float(input("Podaj kwotę regularnej dopłaty: "))
    czestotliwosc = input("Jak często chcesz dokonywać dopłat? (tygodniowo/miesięcznie/kwartalnie/rocznie): ").lower()
else:
    doplata = 0
    czestotliwosc = 'rocznie'

# Obliczenie wartości przyszłej z dopłatami
wynik = procent_składany_z_dopłatami(kwota, procent, lata, doplata, czestotliwosc)

# Wyświetlenie wyniku
if wynik is not None:
    print("Wartość przyszła:", round(wynik, 2))
