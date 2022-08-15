from ex10 import nextPrime

def _10001Prime():
    i = 6
    res = 13
    while i < 10001:
        res = nextPrime(res)
        i += 1
    return res
