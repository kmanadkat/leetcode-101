
# Print the name of candidate that received Max votes. If there is tie, print lexicographically smaller name. Function to return the name of candidate that received maximum votes.
def winner(self, arr, n):
    if n == 1:
        return [arr[0], 1]

    # return the name of the winning candidate and the votes he recieved
    dt = {}
    for ele in arr:
        if ele in dt:
            dt[ele] += 1
        else:
            dt[ele] = 1

    ansArr = [arr[0], 1]
    for ele in dt:
        freq = dt[ele]
        ansFreq = ansArr[1]
        if freq > ansFreq:
            ansArr[0] = ele
            ansArr[1] = freq

        elif freq == ansFreq:
            if ele < ansArr[0]:
                ansArr[0] = ele

    return ansArr
