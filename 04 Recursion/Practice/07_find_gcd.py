
def gcdHelper(a, b, n):
    if n == 1:
        return 1

    if a % n == 0 and b % n == 0:
        return n

    else:
        return gcdHelper(a, b, n-1)


def GCD(a, b):
    return gcdHelper(a, b, min(a, b))
