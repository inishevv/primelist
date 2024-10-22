import math
from typing import Optional

def _is_prime(i) -> bool: #для проверки является ли число простым
    if i < 2:
        return False
    for j in range(3, int(math.sqrt(i) + 1), 2):
        if i % j == 0:
            return False
    return True


def primelist(x: int, y: int) -> Optional[list[int]]:#для формирования списка простых чисел
    m = []

    for i in range(x,y):
        f = 0
        if i % 2 != 0 or i == 2:
            if _is_prime(i):
                m.append(i)
    return m