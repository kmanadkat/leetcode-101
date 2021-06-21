

def nToOne(n):
    if n < 1:
        return

    print(n)
    nToOne(n-1)


def oneToN(n):
    if n < 1:
        return

    oneToN(n - 1)
    print(n)


nToOne(5)
print('\nMethod 2')
oneToN(5)
