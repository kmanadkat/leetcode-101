

def isPanagram(s):
    alphabets = [0] * 26

    for i in range(26):
        if s.find(chr(ord('a') + i)) != -1 or s.find(chr(ord('A') + i)) != -1:
            alphabets[i] = 1

    sumA = 0
    for ele in alphabets:
        sumA += ele

    return 1 if sumA == 26 else 0
