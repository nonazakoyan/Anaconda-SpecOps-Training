'''Հաշվել տրված թվի թվանշանների արտադրյալի և գումարի տարբերությունը։ 
    Օրինակ, տրված է 4637, վերադարձնել (4*6*3*7) - (4+6+3+7)'''

import ex08 as e

def diff(number):
    n = str(number)
    ft_mul = 1

    for i in n:
        ft_mul *= int(i)
    return ft_mul - e.count_dig(number)
