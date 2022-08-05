'''Իրականացնել ծրագիր, որը կհաշվի թե յուրաքանչյուր բառ 
    քանի անգամ է հանդիպում տեքստային ֆայլում։'''

import ex03 as e

def remove_empty_items(lst):
    for i in range(lst.count('')):
        lst.remove('')
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
    return lst
my_dict = {}
file_name = input("input file name: ")
fd = open(file_name, 'r')

buff = fd.read().strip().split(' ')
buff = remove_empty_items(buff)
my_dict = e.my_func(buff)
# print(my_dict)
fd.close