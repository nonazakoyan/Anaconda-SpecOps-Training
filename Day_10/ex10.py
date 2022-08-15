def isprime(num):
    if num in (2, 3, 5, 7):
        return True
    elif num in (4, 6, 8, 9):
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def nextPrime(num):
    while True:
        num += 1
        if isprime(num):
            return num
        
def simpleFactors(num):
    smplFact = []
    prime = 2
    while num > 1:
        flag = False
        if num % prime == 0:
            smplFact.append(prime)
            num /= prime
        else:
            prime = nextPrime(prime)
            num = num
    return smplFact

def SmallestMultiple(number = 20):
    factor = [1]
    mul = 1
    for i in range(2, number + 1):
        if isprime(i):
            factor.append(i)
            mul *= i
        else:
            for j in  (smpFact := simpleFactors(i)):
                if smpFact.count(j) > factor.count(j) or factor.count(j) == 0:
                    factor.append(j)  
                    mul *= j
    return mul
