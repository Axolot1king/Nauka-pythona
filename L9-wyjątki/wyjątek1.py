def dzialanie(a,b):
    try:
        print('qwetyr')
        #print('qwetyr' + 12)
        print(a / b)
        print('qwetyr')
    except (ZeroDivisionError, TypeError) as x:
        print('Łat ar ju dułing? ju dit: ', x)
    #except ZeroDivisionError:
    #except:


divide = dzialanie

divide(2,1)