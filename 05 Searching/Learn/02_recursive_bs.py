

from typing import List


def recursiveHelper(inpLs: List[int], si: int, ei: int, ele: int) -> int:
    if si > ei:
        return -1

    mid = (si + ei) // 2
    if inpLs[mid] == ele:
        return mid

    elif inpLs[mid] > ele:
        return recursiveHelper(inpLs, si, mid - 1, ele)

    elif inpLs[mid] < ele:
        return recursiveHelper(inpLs, mid+1, ei, ele)


def recursiveBs(inpLs: List[int], ele: int) -> int:
    return recursiveHelper(inpLs, 0, len(inpLs)-1, ele)


print(recursiveBs([1, 2, 3, 4, 5], 4))
print(recursiveBs([1, 2, 3, 4, 5], 1))
print(recursiveBs([1, 2, 3, 4, 5], 2))
print(recursiveBs([1, 2, 3, 4, 5], 3))
print(recursiveBs([1, 2, 3, 4, 5], 5))
print(recursiveBs([1, 2, 3, 4, 5, 6], 2))
print(recursiveBs([5, 15, 25], 25))
print(recursiveBs([5, 10, 15, 25, 35], 20))
print(recursiveBs([10, 15], 5))
print(recursiveBs([10, 10], 10))
