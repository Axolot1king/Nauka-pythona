import matplotlib.pyplot as plt

def procent_składany_z_dopłatami(kwota, procent, lata, doplata, czestotliwosc):
    r = procent / 100
    czestotliwosc_map = {'tygodniowo': 52, 't': 52, 'miesięcznie': 12, 'm': 12, 'kwartalnie': 4, 'k': 4, 'rocznie': 1, 'r': 1}
    okresy = czestotliwosc_map.get(czestotliwosc)

    if okresy is None:
        print("Niepoprawna częstotliwość dopłat.")
        return None, None, None

    wartosci_calkowite = []
    suma_doplat = []
    przyszla_wartosc = kwota
    suma_doplat_aktualna = 0
    wartosci_calkowite.append(przyszla_wartosc)
    suma_doplat.append(suma_doplat_aktualna)

    for t in range(1, lata * okresy + 1):
        przyszla_wartosc = przyszla_wartosc * (1 + r / okresy)
        if t % (okresy // czestotliwosc_map[czestotliwosc]) == 0:
            suma_doplat_aktualna += doplata
            przyszla_wartosc += doplata
        wartosci_calkowite.append(przyszla_wartosc)
        suma_doplat.append(suma_doplat_aktualna)

    return wartosci_calkowite, suma_doplat, okresy

# Pobieranie danych od użytkownika z walidacją
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Proszę podać prawidłową liczbę.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Proszę podać prawidłową liczbę całkowitą.")

def get_czestotliwosc(lata):
    if lata <= 10:
        return 'tygodniowo'
    elif lata <= 20:
        return 'kwartalnie'
    elif lata < 30:
        return 'rocznie'
    else:
        return '5l'

kwota = get_float("Podaj kwotę początkową: ")
procent = get_float("Podaj stopę procentową (w %): ")
lata = get_int("Podaj liczbę lat: ")
doplaty = input("Czy chcesz dokonywać regularnych dopłat? (tak/nie): ").lower()

if doplaty == 'tak':
    doplata = get_float("Podaj kwotę regularnej dopłaty: ")
    czestotliwosc = input("Jak często chcesz dokonywać dopłat? (tygodniowo[t]/miesięcznie[m]/kwartalnie[k]/rocznie[r]): ").lower()
else:
    doplata = 0
    czestotliwosc = 'rocznie'

wartosci_calkowite, suma_doplat, okresy = procent_składany_z_dopłatami(kwota, procent, lata, doplata, czestotliwosc)

if wartosci_calkowite is not None and suma_doplat is not None and okresy is not None:
    # Tworzenie wykresu
    x_lata = [i / okresy for i in range(lata * okresy + 1)]
    plt.plot(x_lata, wartosci_calkowite, label='Wartość całkowita', color='b')
    plt.step(x_lata, suma_doplat, label='Łączna suma dopłat', color='orange', where='mid')

    # Dodawanie punktów na koniec każdego roku zgodnie z wymaganiami
    roczne_wartosci = [wartosci_calkowite[i * okresy] for i in range(1, lata + 1)]
    roczne_lata = list(range(1, lata + 1))
    label_shown = False

    for i, rok in enumerate(roczne_lata):
        if lata <= 10 and rok % 1 == 0:
            plt.scatter(rok, roczne_wartosci[i], color='red', zorder=5, label='Wartość na koniec okresu' if not label_shown else "")
            label_shown = True
            plt.text(rok, roczne_wartosci[i], f'{int(roczne_wartosci[i])}', ha='left', va='bottom')
        elif lata <= 20 and rok % 2 == 0:
            plt.scatter(rok, roczne_wartosci[i], color='red', zorder=5, label='Wartość na koniec okresu' if not label_shown else "")
            label_shown = True
            plt.text(rok, roczne_wartosci[i], f'{int(roczne_wartosci[i])}', ha='left', va='bottom')
        elif lata < 30 and rok % 5 == 0:
            plt.scatter(rok, roczne_wartosci[i], color='red', zorder=5, label='Wartość na koniec okresu' if not label_shown else "")
            label_shown = True
            plt.text(rok, roczne_wartosci[i], f'{int(roczne_wartosci[i])}', ha='left', va='bottom')
        elif lata <= 50 and rok % 10 == 0:
            plt.scatter(rok, roczne_wartosci[i], color='red', zorder=5, label='Wartość na koniec okresu' if not label_shown else "")
            label_shown = True
            plt.text(rok, roczne_wartosci[i], f'{int(roczne_wartosci[i])}', ha='left', va='bottom')

    plt.xlabel('Lata')
    plt.ylabel('Wartość')
    plt.title('Wartość przyszła z procentem składanym i dopłatami')
    plt.legend()
    plt.grid(True)
    plt.show()
