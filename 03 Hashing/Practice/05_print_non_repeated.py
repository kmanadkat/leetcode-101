def printNonRepeated(arr, n):
    if n == 1:
        return arr

    dt = {}
    for ele in arr:
        if ele in dt:
            dt[ele] += 1
        else:
            dt[ele] = 1

    opt = []
    for ele in arr:
        if dt[ele] == 1:
            opt.append(ele)

    return opt
