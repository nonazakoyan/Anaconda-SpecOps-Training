'''Գրել ծրագիր, որը հաշվում է 1-ից 100 թվերի գումարի քառակուսին (1+...+100)^2, 
    հաշվում է 1-ից 100 թվերի քառակուսիների գումարը՝ (1^2 + 2^2 + … + 100^2):
    Ծրագիրը տպում է ստացված թվերի տարբերությունը։ '''


def sqr_of_sum(number):
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum ** 2

def sum_of_sqrs(number):
    sum = 0
    for i in range(number + 1):
        sum += i ** 2
    return sum

print(abs(sqr_of_sum(100) - sum_of_sqrs(100)))