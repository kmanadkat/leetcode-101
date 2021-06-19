from typing import List


# Approch 1 -> Using Sets
def findDistinctCount(inputList: List) -> int:
    if len(inputList) <= 1:
        return len(inputList)

    return len(set(inputList))


# Approach 2 -> Using dictionary
def findDistinctCount2(inputList: List) -> int:
    if len(inputList) <= 1:
        return len(inputList)

    d = {}
    for ele in inputList:
        if ele not in d:
            d[ele] = True

    return len(d)


print(findDistinctCount(inputList=[10, 10, 20, 30, 50]))
print(findDistinctCount(inputList=[10]))
print(findDistinctCount(inputList=[10, 20]))
print(findDistinctCount(inputList=[10, 10]))
print(findDistinctCount(inputList=[40, 40, 40]))

print("\nMethod 2")
print(findDistinctCount2(inputList=[10, 10, 20, 30, 50]))
print(findDistinctCount2(inputList=[10]))
print(findDistinctCount2(inputList=[10, 20]))
print(findDistinctCount2(inputList=[10, 10]))
print(findDistinctCount2(inputList=[40, 40, 40]))
