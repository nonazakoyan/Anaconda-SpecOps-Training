def SumSquareDifference(number = 100):
    sum = 0
    sumSqr = 0
    for i in range(1, number + 1):
        sum += i
        sumSqr += i ** 2
    return sum ** 2 - sumSqr

