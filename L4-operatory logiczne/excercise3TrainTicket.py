print('Hello im E-conduktor! Can i see your ticket?')

t = input('dou you have ticket (no-0) if you have trype number of option '
           '\ndepends on kind. (reduced-1, normal-2):')

gd = input('what is your gender (M/F):')

ag = input('what is your age?:')

ID = input('dou you have ID card (no-0) if you have trype number of option '
           '\ndepends on kind. (university ID card-1'
           '\nstudent ID card-2, pension ID card-3 railway worker ID card-4:')
ID = int(ID)

date = input('actual or not?(Y/N):')

if (t == '2' and date == 'Y') or (t == '1' and gd == 'M' and ag >= '65' and ID == '3' and date == 'Y') or (t == '1' and gd == 'F' and ag >= '60' and ID == '3' and date == 'Y') or (t == '1' and ag < '16' and ID == '1' and date == 'Y') or (t == '1' and ID == '2' and date == 'Y'):
    print('you can ride along!')
elif ID == '4':
    print('Hello worker:)')

else:
    print('GET OUT OF THE TRAIN AND PAY MANDATE OF FINE WORTH $1,000!!! (if you survive)')






