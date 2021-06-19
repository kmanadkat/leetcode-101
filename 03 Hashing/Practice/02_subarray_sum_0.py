
from typing import List


# Approach 1 -> o(n^2)
# [0] -> [0, 1] -> [0, 1, 2] -> ... [0, ..., n-1]
# [1] -> [1, 2] -> [1, 2, 3] -> ... [1, ..., n-1]
def subArraySum(inpLs: List) -> bool:
    n = len(inpLs)
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(inpLs[i:j]) == 0:
                return True
    return False


# Approach 2 -> o(n^2) -> inbuit sum for every itr
def subArraySum2(inpLs: List) -> bool:
    dict = {}
    for i in range(len(inpLs)+1):
        if i == 0:
            continue

        pref_sum = sum(inpLs[0:i])
        if pref_sum in dict:
            return True
        else:
            dict[pref_sum] = True

    return False


# Approach 3 -> o(n) -> pre_sum already present for smaller range of numbers
# -> must have negative number to create this situation
def subArraySum3(inpLs: List) -> bool:
    st = set()
    pre_sum = 0
    for i in range(len(inpLs)):
        pre_sum += inpLs[i]
        if pre_sum == 0 or pre_sum in st:
            return True
        else:
            st.add(pre_sum)

    return False


print(subArraySum(inpLs=[-3, 4, -3, -1, 1]))
print(subArraySum2(inpLs=[-3, 4, -3, -1, 1]))
print(subArraySum3(inpLs=[-3, 4, -3, -1, 1]))

print(subArraySum(inpLs=[4, 3, -2, 1, 1]))
print(subArraySum2(inpLs=[4, 3, -2, 1, 1]))
print(subArraySum3(inpLs=[4, 3, -2, 1, 1]))
