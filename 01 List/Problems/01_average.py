
from typing import List


def findListAverage(inputList: List) -> int:
    sizeOfList = len(inputList)
    sumOfList = sum(inputList)
    return sumOfList / sizeOfList


print(findListAverage(inputList=[0, 1, 2, 3, 4, 5, 6]))
