from math import floor as __floor, sqrt as __sqrt


def factorize(n):
    if n < 0:
        raise ValueError('Can only factorize Natural numbers')
    if n < 2:
        return [n]
    for i in range(2, __floor(__sqrt(n)) + 1):
        if n % i == 0:
            return [i] + factorize(n // i)
    return [n]
