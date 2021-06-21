

def sumOfDigits(n):
    if n <= 9:
        return n

    recAns = sumOfDigits(n//10)
    return recAns + (n % 10)


print(sumOfDigits(984))
