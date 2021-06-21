
def towerOfHanoi(n, source, auxiliary, destination):
    if n == 0:
        return 0
    # Move n-1 from source to auxiliary using destination
    stepCnt1 = towerOfHanoi(n-1, source, destination, auxiliary)

    # Move nth disc from source to destination
    print(f"{n} {source} -> {destination}")

    # move n-1 from auxiliary to destination using source
    stepCnt2 = towerOfHanoi(n-1, auxiliary, source, destination)

    # Return Total Number of Steps
    return 1 + stepCnt1 + stepCnt2


towerOfHanoi(10, "A", "B", "C")
