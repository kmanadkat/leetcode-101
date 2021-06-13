from typing import List


# Approach 1 - Simple List
def getSmaller(number: int, inputList: List) -> List:
    smallerList = []
    for element in inputList:
        if element < number:
            smallerList.append(element)

    return smallerList


# Approach 2 - List Comprehension
def getSmallerComprehension(number: int, inputList: List) -> List:
    return [x for x in inputList if x < number]


print(getSmaller(number=60, inputList=[100, 20, 40, 60, 80, 200]))
print(getSmallerComprehension(number=60, inputList=[100, 20, 40, 60, 80, 200]))
