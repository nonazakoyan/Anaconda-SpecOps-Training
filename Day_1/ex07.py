'''Գրել ծրագիր, որը կհաշվի տրված զանգվածի արժեքների քառակուսիները 
    և կպահի դրանք նոր զանգվածում՝ սորտավորված ձևով։'''

def srq_items(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i**2)
    new_lst.sort()
    return new_lst
