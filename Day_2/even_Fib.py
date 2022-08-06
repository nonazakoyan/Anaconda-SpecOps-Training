def iseven(number):
    if number % 2 == 0:
        return True
    return False

def even_fib(number):
    fib1 = 1
    fib2 = 2
    sum  = 0
    while(fib1 < number):
        if iseven(fib1):
            sum += fib1
        res = fib1 + fib2
        fib2, fib1 = res, fib2
    return sum
print(even_fib(100))