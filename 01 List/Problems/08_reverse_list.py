

from typing import List


# Approach 1 -> Slicing Method
def reverseList(inputList: List) -> List:
    if(len(inputList) <= 1):
        return inputList

    return inputList[:: -1]


# Approach 2 -> Inbuilt Method
def reverseList2(inputList: List) -> List:
    if(len(inputList) <= 1):
        return inputList

    inputList.reverse()
    return inputList


# Approach 3 -> RAW SWAPPING :)
def reverseList3(inputList: List) -> List:
    if(len(inputList) <= 1):
        return inputList

    lastIndex = len(inputList) - 1
    startIndex = 0
    while startIndex < lastIndex:
        inputList[startIndex], inputList[lastIndex] = inputList[lastIndex], inputList[startIndex]
        startIndex += 1
        lastIndex -= 1
    return inputList


print(reverseList(inputList=[10, 20, 30, 40, 19, 21]))
print(reverseList(inputList=[10]))
print(reverseList(inputList=[10, 20]))

print("\nMethod 2")
print(reverseList2(inputList=[10, 20, 30, 40, 19, 21]))
print(reverseList2(inputList=[10]))
print(reverseList2(inputList=[10, 20]))

print("\nMethod 3")
print(reverseList3(inputList=[10, 20, 30, 40, 19, 21]))
print(reverseList3(inputList=[10]))
print(reverseList3(inputList=[10, 20]))
