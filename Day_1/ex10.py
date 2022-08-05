'''Գրել ֆունկցիա, որը ստանում է միջակայքի սկիզբ և վերը (երկու թվեր) 
    և հաշվում միջակայքում գտնվող կենտ թվերի քանակը։ '''

def range_odd(start, end):
    if start <= end:
        count = 0
        ft_range = end - start + 1
        if start % 2 == 1 and end % 2 == 1:
            return ft_range // 2 + 1
        return ft_range // 2
    return -1
print(range_odd(15, 2))