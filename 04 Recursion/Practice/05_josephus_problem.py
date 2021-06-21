

def jso(n, k) -> int:

    arr = [x for x in range(1, n+1)]
    idx = 0
    while len(arr) > 1:
        idx = (idx + k - 1) % len(arr)
        arr.pop(idx)
        if idx == len(arr):
            idx = 0
    return arr[0]


def jso2(n: int, k: int) -> int:
    if n == 1:
        return 0

    return (jso(n-1, k) + k) % n


print(jso(6, 5))
print(jso2(6, 5))
