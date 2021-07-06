
from typing import List


def binarySearch(inpLs: List[int], ele: int) -> int:
    if len(inpLs) == 0:
        return -1

    si = 0
    ei = len(inpLs) - 1
    while si <= ei:
        mid = (si + ei) // 2
        if inpLs[mid] == ele:
            return mid

        elif inpLs[mid] > ele:
            ei = mid - 1

        elif inpLs[mid] < ele:
            si = mid + 1

    return -1


print(binarySearch([1, 2, 3, 4, 5], 4))
print(binarySearch([1, 2, 3, 4, 5], 1))
print(binarySearch([1, 2, 3, 4, 5], 2))
print(binarySearch([1, 2, 3, 4, 5], 3))
print(binarySearch([1, 2, 3, 4, 5], 5))
print(binarySearch([1, 2, 3, 4, 5, 6], 2))
print(binarySearch([5, 15, 25], 25))
print(binarySearch([5, 10, 15, 25, 35], 20))
print(binarySearch([10, 15], 5))
print(binarySearch([10, 10], 10))
