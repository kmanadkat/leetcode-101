

# Appraoch 1 : Sorting, Joining & Compare -> O(nLogn)
def checkIfAnagram1(inp1: str, inp2: str) -> bool:
    if(len(inp1) != len(inp2)):
        return False
    inp1Sorted = "".join(sorted(inp1))
    inp2Sorted = "".join(sorted(inp2))
    return inp1Sorted == inp2Sorted


# Approach 2: Using Xor :P (Smart boooy) -> O(n)
def checkIfAnagram2(inp1: str, inp2: str) -> bool:
    if(len(inp1) != len(inp2)):
        return False

    xorOp = 0
    for ele in inp1:
        xorOp = xorOp ^ ord(ele)

    for ele in inp2:
        xorOp = xorOp ^ ord(ele)

    return xorOp == 0


print(checkIfAnagram1("listen", "silent"))
print(checkIfAnagram1("aacb", "acab"))
print(checkIfAnagram1("axb", "aby"))

print("\nMethod 2: ")
print(checkIfAnagram1("listen", "silent"))
print(checkIfAnagram1("aacb", "acab"))
print(checkIfAnagram1("axb", "aby"))
