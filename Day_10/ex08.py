def isprime(num):
    if num in (2,3,5,7):
        return True
    elif num in (4, 6, 8, 9):
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def largestPrimeFactor(number):
    res = -1
    for i in range(2, int(number ** .5)):
        if isprime(i) and number % i == 0:
            res = i
    return res

print(largestPrimeFactor(600851475143))

