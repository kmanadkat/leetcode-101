

# Approach 1: Using Loop
def checkIfPalindrome1(inpStr: str) -> str:
    si = 0
    ei = len(inpStr) - 1

    while si < ei:
        if(inpStr[si] != inpStr[ei]):
            return 'No'
        si += 1
        ei -= 1

    return 'Yes'


# Approach 2: Using Slicing - Super Short
def checkIfPalindrome2(inpStr: str) -> str:
    return 'Yes' if inpStr == inpStr[::-1] else 'No'


print(checkIfPalindrome1("abba"))
print(checkIfPalindrome1("abcba"))
print(checkIfPalindrome1("a"))
print(checkIfPalindrome1(""))
print(checkIfPalindrome1("geek"))
print(checkIfPalindrome1("Aba"))

print("\nMethod 2: ")
print(checkIfPalindrome2("abba"))
print(checkIfPalindrome2("abcba"))
print(checkIfPalindrome2("a"))
print(checkIfPalindrome2(""))
print(checkIfPalindrome2("geek"))
print(checkIfPalindrome2("Aba"))
