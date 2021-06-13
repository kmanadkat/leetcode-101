

from typing import List


# Helper Function
def reverseList(sI: int, eI: int, l: List):
    while sI < eI:
        l[sI], l[eI] = l[eI], l[sI]
        sI += 1
        eI -= 1


# Apporach 1 -> Efficient -> Linear & in Place
def leftRotateByN(inputList: List, n: int) -> List:
    inputLen = len(inputList)
    moduloN = n % inputLen
    if (inputLen <= 1 or moduloN == 0):
        return inputList

    # Rotate first n elements
    reverseList(0, moduloN - 1, inputList)

    # rotate from n+1 till end
    reverseList(moduloN, inputLen - 1, inputList)

    # rotate whole
    reverseList(0, inputLen - 1, inputList)
    return inputList


# Apporach 2 -> Slicing -> Linear & extra space
def leftRotateByN2(inputList: List, n: int) -> List:
    inputLen = len(inputList)
    moduloN = n % inputLen
    if (inputLen <= 1 or moduloN == 0):
        return inputList

    l = inputList[moduloN:] + inputList[: moduloN]
    return l


# Apporach 3 -> inbuilt pop -> O(n2)
def leftRotateByN3(inputList: List, n: int) -> List:
    inputLen = len(inputList)
    moduloN = n % inputLen
    if (inputLen <= 1 or moduloN == 0):
        return inputList

    idx = 0
    while idx < moduloN:
        inputList.append(inputList.pop(0))
        idx += 1

    return inputList


print(leftRotateByN(inputList=[10, 20, 30, 40, 50], n=1))
print(leftRotateByN(inputList=[10, 20, 30, 40, 50], n=2))
print(leftRotateByN(inputList=[10, 20, 30, 40, 50], n=3))
print(leftRotateByN(inputList=[10, 20, 30, 40, 50], n=6))
print(leftRotateByN(inputList=[10, 20], n=6))
print(leftRotateByN(inputList=[10], n=4))

print('\nMethod 2')
print(leftRotateByN2(inputList=[10, 20, 30, 40, 50], n=1))
print(leftRotateByN2(inputList=[10, 20, 30, 40, 50], n=2))
print(leftRotateByN2(inputList=[10, 20, 30, 40, 50], n=3))
print(leftRotateByN2(inputList=[10, 20, 30, 40, 50], n=6))
print(leftRotateByN2(inputList=[10, 20], n=6))
print(leftRotateByN2(inputList=[10], n=4))

print('\nMethod 3')
print(leftRotateByN3(inputList=[10, 20, 30, 40, 50], n=1))
print(leftRotateByN3(inputList=[10, 20, 30, 40, 50], n=2))
print(leftRotateByN3(inputList=[10, 20, 30, 40, 50], n=3))
print(leftRotateByN3(inputList=[10, 20, 30, 40, 50], n=6))
print(leftRotateByN3(inputList=[10, 20], n=6))
print(leftRotateByN3(inputList=[10], n=4))
