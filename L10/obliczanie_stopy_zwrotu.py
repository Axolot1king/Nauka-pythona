def procent_składany(kwota, procent, lata):
    # Zamiana procentu na ułamek dziesiętny
    r = procent / 100
    # Obliczenie wartości przyszłej
    przyszła_wartość = kwota * (1 + r) ** lata
    return przyszła_wartość

# Przykładowe dane wejściowe
kwota = float(input("Podaj kwotę początkową: "))
procent = float(input("Podaj stopę procentową (w %): "))
lata = int(input("Podaj liczbę lat: "))

wynik = procent_składany(kwota, procent, lata)
print("Wartość przyszła:", wynik)
print(f"Przyszła wartość  {wynik:.2f} zł.")
