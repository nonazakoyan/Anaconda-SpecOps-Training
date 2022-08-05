'''Իրականացնել ֆունկցիա, որը կհեռացնի 
    ստացված տողի (string) ամեն երրորդ սիմվոլը։'''

def chrdel(ft_str, index):
    new_str = ft_str[: index] + ft_str[index + 1:]
    return new_str

ft_str = input("input: ")

str_len = len(ft_str)
k = 0
for i in range(0, str_len):
    if i % 3 == 2:
        ft_str = chrdel(ft_str, i - k)
        k += 1
print(ft_str)