# Function to check if there is a pair with the given sum in the array.
def sumExists(arr, N, sum):
    if N <= 1:
        return 0

    dt = {}
    for ele in arr:
        compNum = sum - ele
        if compNum in dt:
            return 1
        dt[ele] = True

    return 0
