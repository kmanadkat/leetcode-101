
from typing import List


# Approach 1 -> Single Iteration
def isNonDecreasing(inputList: List) -> bool:
    if(len(inputList) <= 1):
        return True

    prevElement = inputList[0]
    for i, element in enumerate(inputList):
        if i == 0:
            continue
        if element < prevElement:
            return False
        prevElement = element
    return True


# Approach 2 -> Single Iteration, Memory optimization
def isNonDecreasing2(inputList: List) -> bool:
    if(len(inputList) <= 1):
        return True

    for i, element in enumerate(inputList):
        if i == 0:
            continue
        if element < inputList[i-1]:
            return False
    return True


# Approach 3 -> Inbuilt functions -> Less Efficient
def isNonDecreasing3(inputList: List) -> bool:
    if(len(inputList) <= 1):
        return True

    sortedList = sorted(inputList)
    return True if sortedList == inputList else False


print(isNonDecreasing(inputList=[10, 20, 30]))
print(isNonDecreasing(inputList=[10, 20, 20, 30]))
print(isNonDecreasing(inputList=[10, 20, 11, 30]))
print(isNonDecreasing(inputList=[10]))
print(isNonDecreasing(inputList=[]))
print(isNonDecreasing(inputList=[10, 5, 30]))

print(isNonDecreasing2(inputList=[10, 20, 30]))
print(isNonDecreasing2(inputList=[10, 20, 20, 30]))
print(isNonDecreasing2(inputList=[10, 20, 11, 30]))
print(isNonDecreasing2(inputList=[10]))
print(isNonDecreasing2(inputList=[]))
print(isNonDecreasing2(inputList=[10, 5, 30]))

print(isNonDecreasing3(inputList=[10, 20, 30]))
print(isNonDecreasing3(inputList=[10, 20, 20, 30]))
print(isNonDecreasing3(inputList=[10, 20, 11, 30]))
print(isNonDecreasing3(inputList=[10]))
print(isNonDecreasing3(inputList=[]))
print(isNonDecreasing3(inputList=[10, 5, 30]))
