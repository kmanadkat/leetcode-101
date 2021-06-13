from typing import List, Tuple


# Approach 1 - Simpler
def separateEvenOdd(inputList: List) -> Tuple:
    even = []
    odd = []
    for element in inputList:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    return even, odd


# Approach 2 - List Comprehensions
def separateEvenOddComprehension(inputList: List) -> Tuple:
    even = [x for x in inputList if x % 2 == 0]
    odd = [x for x in inputList if x % 2 != 0]
    return even, odd


even1, odd1 = separateEvenOdd(inputList=[10, 41, 30, 15, 80])
print(even1)
print(odd1)


even2, odd2 = separateEvenOddComprehension(inputList=[10, 41, 30, 15, 80])
print(even2)
print(odd2)
