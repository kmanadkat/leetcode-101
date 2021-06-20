# Function to find the first non-repeating character in a string.
def nonrepeatingCharacter(s):
    if len(s) <= 1:
        return s

    dt = {}
    for ele in s:
        if ele in dt:
            dt[ele] += 1
        else:
            dt[ele] = 1

    for ele in s:
        if dt[ele] == 1:
            return ele

    return '$'
