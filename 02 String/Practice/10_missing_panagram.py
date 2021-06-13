

def missingPanagram(s):
    alphabets = [chr(ord('a') + i) for i in range(26)]
    outStr = ''

    for ele in alphabets:
        if s.find(ele) == -1 and s.find(ele.upper()) == -1:
            outStr += ele

    return -1 if len(outStr) == 0 else outStr
