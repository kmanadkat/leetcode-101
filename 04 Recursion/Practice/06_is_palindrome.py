
# Approach 1
def isPalindrome(inpStr, si, ei):
    if si >= ei:
        return True

    if inpStr[si] != inpStr[ei]:
        return False

    else:
        return isPalindrome(inpStr, si + 1, ei - 1)


def isPalin(N):
    strNum = str(N)
    return 1 if isPalindrome(strNum, 0, len(strNum) - 1) else 0


# Approach 2: Reverse Number
