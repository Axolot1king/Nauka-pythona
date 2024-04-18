x = int(input('Enter number : '))

def silnia(X):
    if X == 1:
        return 1
    else:
        return X * silnia(X - 1)

print(silnia(x))
