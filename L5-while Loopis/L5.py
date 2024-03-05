x = 1
while x <= 15:
    if x % 2 == 0:
        print('Parzy!!!')
    x += 1
    if x == 3:
        continue
    print(f'aktualna liczba {x}, w następnej pętli będzie {x + 1}')
    if x >= 10:
        break
print('koŃ')