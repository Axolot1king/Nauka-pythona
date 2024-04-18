import runpy


# noinspection PyStatementEffect
def BMI():
    wzrosT = float(input("What is ur height [meters]? : "))
    nasA = float(input("What is ur weight [kilos]? : "))

    def BMIv2(nasa, wzrost):
        return nasa / wzrost **2

    print('bmi test result is : ', BMIv2(nasA, wzrosT))

    number = float(input('enter your BMI test number : '))


    if number < 18.5:
        print('You have underweight! you must eat a lil bit more'
              '\nor you can have some problems')

    elif 18.5 <= number <= 24.9:
        print('You have normal weight! you basically perfect (in mass)')

    elif 25.0 <= number <= 29.9:
        print("You have pre-obesity! go run for 2 hours daily for 5 days and"
              "\ncheck again if it's go higher you may have issues")

    elif 30.0 <= number <= 34.9:
        print('You have obesity class I! go to gym for 2.5 hours '
              '\nand eat mostly salads you closer to have really big'
              '\nissues')

    elif 35.0 <= number <= 39.9:
        print('you have obesity class II! no really go to gym '
              '\nfor 5 or 4 hours and eat healthy food you really close to have'
              '\nsome really issues so: stop it, get some help')

    elif number > 40.0:
        print('you have obesity class III! well you probably have issues already'
              '\nso go to doctor or somewhere he may help you =)')



while True:
    BMI()
    x = input('do u wont to do another test (yes/no)? : ')
    if x.lower() != 'yes':
        print('sayonara')
        break
