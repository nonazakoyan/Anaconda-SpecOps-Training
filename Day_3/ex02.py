'''Տրված է անուններ պարունակող ֆայլը ,
    (https://projecteuler.net/project/resources/p022_names.txt)
    արտագրել արժեքները մեկ այլ ֆայլում, որտեղ մեծատառով կլինեն միայն 
    անունների առաջին տառերը։'''

fd = open("p022_names.txt", 'r')
fd1 = open("output.txt", "w")
buff = fd.read().replace('"', '').split(',')

for i in buff:
    k = '"' + i.title() + '", '
    fd1.write(k)

fd.close()
fd1.close()