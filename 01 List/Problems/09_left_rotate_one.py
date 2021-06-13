

from typing import List


# Approach 1 : Inbuilt functions pop/del & append
def leftRotateByOne(inputList: List) -> List:
    if(len(inputList) <= 1):
        return inputList

    firstEle = inputList.pop(0)
    inputList.append(firstEle)

    return inputList


# Approach 2 : RAW method :)
def leftRotateByOne2(inputList: List) -> List:
    listLength = len(inputList)
    if(listLength <= 1):
        return inputList

    firstEle = inputList[0]

    for idx, _ in enumerate(inputList):
        if idx + 1 < listLength:
            inputList[idx] = inputList[idx + 1]

    inputList[listLength - 1] = firstEle

    return inputList


print(leftRotateByOne(inputList=[10, 20, 30, 40, 19, 21]))
print(leftRotateByOne(inputList=[10]))
print(leftRotateByOne(inputList=[10, 20]))

print("\nMethod 2")
print(leftRotateByOne2(inputList=[10, 20, 30, 40, 19, 21]))
print(leftRotateByOne2(inputList=[10]))
print(leftRotateByOne2(inputList=[10, 20]))
