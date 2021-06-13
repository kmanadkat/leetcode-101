
from typing import List


# Approach 1 - 2 Traversals
def getSecondLargest(inputList: List[int]) -> int:
    if(len(inputList) <= 1):
        return None

    maxElement = max(inputList)
    secondMax = min(inputList)
    for element in inputList:
        if element > secondMax and element < maxElement:
            secondMax = element

    return None if secondMax == maxElement else secondMax


# Approach 2 - 2 Traversals
def getSecondLargest2(inputList: List[int]) -> int:
    if(len(inputList) <= 1):
        return None

    maxElement = max(inputList)
    secondMax = None
    for element in inputList:
        if element != maxElement:
            if secondMax == None:
                secondMax = element
            else:
                secondMax = max(element, secondMax)

    return secondMax


# Approach 3 - Single Traversal
def getSecondLargest3(inputList: List) -> int:
    if(len(inputList) <= 1):
        return None

    maxEle = None
    secondMax = None
    for element in inputList:
        if maxEle == None:
            maxEle = element
        else:
            if element > maxEle:
                secondMax = maxEle
                maxEle = element
            if element < maxEle:
                if secondMax == None:
                    secondMax = element
                elif secondMax < element:
                    secondMax = element
    return secondMax


print(getSecondLargest(inputList=[10, 5, 8, 20]))
print(getSecondLargest(inputList=[20, 10, 20, 8, 12]))
print(getSecondLargest(inputList=[10, 10, 10]))

print(getSecondLargest2(inputList=[10, 5, 8, 20]))
print(getSecondLargest2(inputList=[20, 10, 20, 8, 12]))
print(getSecondLargest2(inputList=[10, 10, 10]))

print(getSecondLargest3(inputList=[10, 5, 8, 20]))
print(getSecondLargest3(inputList=[20, 10, 20, 8, 12]))
print(getSecondLargest3(inputList=[10, 10, 10]))
