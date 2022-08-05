'''Հաշվել տրված թվի թվանշանների գումարը։ 
    Օրինակ, տրված է 4637, վերադարձնել 4+6+3+7'''

def count_dig(number):
    n = str(number)
    ft_sum = 0

    for i in n:
        ft_sum += int(i)
    return ft_sum
