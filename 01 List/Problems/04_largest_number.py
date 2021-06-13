from typing import List


# Approach 1
def getLargestNumber(inputList: List[int]) -> int:
    if(len(inputList) <= 0):
        return None
    largest = inputList[0]
    for element in inputList:
        largest = element if element > largest else largest
    return largest


# Approach 2
def getLargestNumber2(inputList: List[int]) -> int:
    if(len(inputList) <= 0):
        return None
    return max(inputList)


print(getLargestNumber(inputList=[10, 5, 20, 8]))
print(getLargestNumber(inputList=[30, 30, 20]))
print(getLargestNumber(inputList=[40]))
print(getLargestNumber(inputList=[]))


print(getLargestNumber2(inputList=[10, 5, 20, 8]))
print(getLargestNumber2(inputList=[30, 30, 20]))
print(getLargestNumber2(inputList=[40]))
print(getLargestNumber2(inputList=[]))
