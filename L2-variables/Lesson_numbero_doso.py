var1 = 'jakiś tam text'
var2 = '6'
var3 = 6
var4 = 0.5

# konkatonacja
# TODO wyświetlić var1 + var1 tak żeby dało się to odczytać
print(var1 + ', ' + var1)
# print(var1 + var3) - nie zadziała ze względu na konflikt zmiennych
print(var1 + var2)
print((var1 + ', ') * var3)
print(var3 * var4)

varMożeszNazwaćJakChcesz = var2 + var2

print(varMożeszNazwaćJakChcesz)
var2 = var3 + var4 + 9
print (var2)

var5 = 'światowych którą przekazała ciotka od strony babci prababci wujka zbigniewa'

print(f'Herbata lipton to numer {var3} najlepszych herbat na świecie! W {var2} roku została nominowana do {var4} nagród {var5}')


var1 = 3
#var1 = var1 + var1
#var1 += var1
var1 *= var1


print(var1)

del(var1)
"""
zapis specjalny dla dłuższych ciągów znaków:
print(f'dowolny txt {nazwa zmiennej} dowolny txt {nazwa zmiennej}')

istnieje też możliwość skróconego zapisywania działań:
- +=
- *=
- -=
- /=
"""

