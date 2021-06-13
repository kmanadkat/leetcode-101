
# Approach 1
def reverseString1(inpStr: str) -> str:
    optStr = inpStr[::-1]
    return optStr


# Approach 2
def reverseString2(inpStr: str) -> str:
    optStr = ""
    for ele in inpStr:
        optStr = ele + optStr
    return optStr


print(reverseString1("krupesh"))
print(reverseString2("krupesh"))
