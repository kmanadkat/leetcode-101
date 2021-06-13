
from typing import List


# Aproach 1 : Using Count inbuilt function
def findOddCountNumber(inputList: List) -> int:
    if (len(inputList) <= 0):
        return None

    for element in inputList:
        freq = inputList.count(element)
        if freq % 2 != 0:
            return element
    return None


# Approach 2 : XOR -> Bitwise Operator -> single itr -> eff
# x XOR x = 0
# x XOR 0 = x
# 0 XOR 1 = 1
# 1 XOR 1 = 0
def findOddCountNumber2(inputList: List) -> int:
    if (len(inputList) <= 0):
        return None

    ans = 0
    for element in inputList:
        ans = ans ^ element
    return ans


print(findOddCountNumber(inputList=[10, 30, 30, 10, 30, 30, 20]))
print(findOddCountNumber(inputList=[10, 10, 10, 10, 10, 20, 20]))
print(findOddCountNumber(inputList=[10, 10, 20, 30, 30, 20, 40]))
print(findOddCountNumber(inputList=[10]))

print("\nmethod 2")
print(findOddCountNumber2(inputList=[10, 30, 30, 10, 30, 30, 20]))
print(findOddCountNumber2(inputList=[10, 10, 10, 10, 10, 20, 20]))
print(findOddCountNumber2(inputList=[10, 10, 20, 30, 30, 20, 40]))
print(findOddCountNumber2(inputList=[10]))
