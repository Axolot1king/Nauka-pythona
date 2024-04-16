def meters_to_inches(meters):
    return meters * 39.3701

def inches_to_meters(inches):
    return inches / 39.3701

def convert_units():
    choice = input("Do you want to convert from meters to inches (m) or from inches to meters (i)? Enter 'm' or 'i': ")
    if choice.lower() == 'm':
        value = float(input("Enter the value in meters: "))
        inches_value = meters_to_inches(value)
        print(f"{value} meters is equal to {inches_value:.2f} inches.")
        print(f"The square of {value} meters is {value**2:.2f} square meters.")
        print(f"The cube of {value} meters is {value**3:.2f} cubic meters.")
    elif choice.lower() == 'i':
        value = float(input("Enter the value in inches: "))
        meters_value = inches_to_meters(value)
        print(f"{value} inches is equal to {meters_value:.2f} meters.")
        print(f"The square of {value} inches is {value**2:.2f} square inches.")
        print(f"The cube of {value} inches is {value**3:.2f} cubic inches.")
    else:
        print("Invalid choice.")


while True:
    convert_units()
    again = input("Do you want to perform another conversion? (yes/no): ")

    if again.lower() != 'yes':
        print("Goodbye!")
        break


