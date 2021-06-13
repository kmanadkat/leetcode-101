

def caseChecker(s, startC, endC):
    for char in s:
        if char >= startC and char <= endC:
            return True

    return False


def validate(s):
    # Length >= 10
    if len(s) < 10:
        return 0

    # Check 1 numeric
    isNumeric = False
    for num in range(10):
        if str(num) in s:
            isNumeric = True
    if not isNumeric:
        return 0

    # Check UpperCase
    isUpper = caseChecker(s, 'A', 'Z')
    if not isUpper:
        return 0

    # Check LowerCase
    isLower = caseChecker(s, 'a', 'z')
    if not isLower:
        return 0

    # Check Special
    isSpecial = False
    chars = ['@', '#', '$', '-', '*']
    for char in chars:
        if s.find(char) != -1:
            isSpecial = True
            break

    if not isSpecial:
        return 0

    return 1
