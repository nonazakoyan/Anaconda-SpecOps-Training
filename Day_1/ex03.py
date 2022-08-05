'''Օգտագործելով աղյուսակ (dictionary) 
    հաշվել զանգվածում բոլոր թվերի կրկնությունների քանակը։'''

def my_func(lst):
    my_dict = {}
    for i in lst:
        my_dict[f'{i}'] = lst.count(i)
    return my_dict
