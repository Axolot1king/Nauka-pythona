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
    print('you need to wait ' + str(21 - wk) + 'years')

else:
    print('you can apply for the position of MP!')

if wk >= 35:
    print('you can run for president')

else:
    print("you can't run for president")
    print('you need to wait ' + str(35 - wk) + 'years')

if wk >= 60:
    if pl == 'F':
        print('you can apply for a pension!')

else:
    print('you need to wait ' + str(60 - wk) + 'years')

if wk >= 65:
    if pl == 'M':
        print('you can apply for a pension!')

else:
    print('you need to wait ' + str(65 - wk) + 'years')

prw = input('do u have driving licence '
            '\nof category A2 at least 2 '
            '\nyears? (yes/no):')

if prw == 'yes':
    if wk >= 20:
        print('you can do driving licence '
              '\nof category A')
    else:
        print("you can't do driving licence of category A ")
        print('you need to wait ' + str(20 - wk) + 'years')



if prw == 'no':
    if wk >= 24:
        print('you can do driving licence '
              '\nof category A')
    else:
        print("you can't do driving licence of category A ")
        print('you need to wait ' + str(24 - wk) + 'years')

if wk >= 18:
    print('you can do driving licence of category B')
else:
    print("you can't do driving licence of category B")
    print('you need to wait ' + str(18 - wk) + 'years')

if wk >= 16:
    print('you can do driving licence of category B1')
else:
    print("you can't do driving licence of category B1")
    print('you need to wait ' + str(16 - wk) + 'years')




