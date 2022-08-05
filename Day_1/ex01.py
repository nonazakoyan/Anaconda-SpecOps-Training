'''Տրված ֆայլում պարունակվում են թվեր։ Իրականացնել ծրագիր, 
    որը հաշվում և վերադարձնում է ֆայլում պարունակվող թվերի գումարը։'''

def ft_sum(buff):
    sum = 0
    for i in buff:
        i = i.strip()
        if i.count('.') == 1:
            sum += float(i)
        elif i.count('.') == 0:
            sum += int(i)
        else: 
            return "Anvalid number"
    return sum

file_name = input("input the file name: ")
fd = open(file_name, 'r')
buff = fd.read().strip().replace('\n', ' ').split(',')
ft_sum(buff)
fd.close()
