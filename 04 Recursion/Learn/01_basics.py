
from typing import NoReturn


def printMessage(n) -> NoReturn:
    # Base Case
    if n <= 0:
        return

    # Single Task
    print('GFG')

    # Recursion's Task
    printMessage(n-1)


printMessage(5)
