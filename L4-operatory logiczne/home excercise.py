haslo = input('write new password:')
comfirm = input('comfirm your password:')
if comfirm == haslo:
    print('you can enter!')

else:
    print('you have second try!')
    comfirm2 = input('confirm your password:')

    if comfirm2 == haslo:
        print('you can enter!')

    else:
        print('you have last try!')
        comfirmm = input('confirm your password:')

        if comfirmm == haslo:
            print('you can enter!')

        else:
            print('you faild the test!')