
def countNonRepeated(arr, n):
    if n <= 1:
        return n

    dt = {}
    for ele in arr:
        if ele in dt:
            dt[ele] += 1
        else:
            dt[ele] = 1

    distinctCount = 0
    for ele in dt:
        if dt[ele] == 1:
            distinctCount += 1

    return distinctCount
