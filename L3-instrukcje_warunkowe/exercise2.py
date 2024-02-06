im = input('what is your first name? :')
nz = input('what is your last name? :')
print('hello! ' + im + ' ' + nz)
pl = input('what is your gender?(F/M) :')
wk = input('how old are you? :')
wk = float(wk)

if wk >= 18:
    print('you can:Buy energy drinks, '
          '\ndigital content for adults, '
          '\nalcohol and cigarettes')

else:
    print("you can't:Buy energy drinks, "
          "\ndigital content for adults, "
          "\nalcohol and cigarettes")
    print('you need to wait ' + str(18 - wk) + 'years')
if wk < 21:
    print('you cannot apply for the position of MP')

else:
    print('you can apply for the position of MP!')

if wk >= 60:
    if pl == 'F':
        print('możesz ubiegać się o emeryturę!')

if wk >= 65:
    if pl == 'M':
        print('możesz ubiegać się o emeryturę!')