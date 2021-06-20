from typing import List
from collections import Counter


# Approach 1: Using dictionary
def isPermutationPalindrome(inpLs: List) -> bool:
    n = len(inpLs)
    if n <= 1:
        return True

    dt = {}
    for ele in inpLs:
        if ele in dt:
            dt[ele] += 1
        else:
            dt[ele] = 1

    oddOccurrences = 0
    for ele in dt:
        if dt[ele] % 2 == 1:
            oddOccurrences += 1
            if oddOccurrences > 1:
                return False
    return True


# Approach 2: Using Inbuilt Counter
def isPermutationPalindrome2(inpLs: List) -> bool:
    cnt = Counter(inpLs)
    oddCount = 0
    for eleFreq in cnt.values():
        if eleFreq % 2 == 1:
            oddCount += 1
            if oddCount > 1:
                return False
    return True


print('geek', isPermutationPalindrome(inpLs="geek"))
print('abc', isPermutationPalindrome(inpLs="abc"))
print('abcba', isPermutationPalindrome(inpLs="abcba"))
print('abbac', isPermutationPalindrome(inpLs="abbac"))
print('abbaccc', isPermutationPalindrome(inpLs="abbaccc"))  # abc c cba
print('abbabb', isPermutationPalindrome(inpLs="abbabb"))
print('abbabbc', isPermutationPalindrome(inpLs="abbabbc"))

print('\nMethod 2')
print('geek', isPermutationPalindrome2(inpLs="geek"))
print('abc', isPermutationPalindrome2(inpLs="abc"))
print('abcba', isPermutationPalindrome2(inpLs="abcba"))
print('abbac', isPermutationPalindrome2(inpLs="abbac"))
print('abbaccc', isPermutationPalindrome2(inpLs="abbaccc"))  # abc c cba
print('abbabb', isPermutationPalindrome2(inpLs="abbabb"))
print('abbabbc', isPermutationPalindrome2(inpLs="abbabbc"))
