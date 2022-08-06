def sum_of_mult(number):
    sum = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_of_mult(10))
print(sum_of_mult(1000))