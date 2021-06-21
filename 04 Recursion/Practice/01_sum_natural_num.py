

# With Recursion
def sumNatural(n):
    if n <= 0:
        return 0

    return n + sumNatural(n-1)


# With Formula
def sumNatural2(n):
    if n <= 0:
        return 0
    return int((n * (n+1)) / 2)


print(sumNatural(10))
print(sumNatural2(10))
