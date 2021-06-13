
from typing import List


def findAllOccurences(inputStr: str, substr: str) -> List[int]:
    if(len(inputStr) <= 0):
        return []

    si = 0
    ei = len(inputStr)
    matchIndices = []
    while si < ei:
        matchIndex = inputStr.find(substr, si)
        if(matchIndex == -1):
            return matchIndices
        matchIndices.append(matchIndex)
        si = matchIndex + 1

    return matchIndices


print(findAllOccurences("In cryptography, encryption is the process of encoding information. This process converts the original representation of the information, known as plaintext, into an alternative form known as ciphertext.", "c"))
