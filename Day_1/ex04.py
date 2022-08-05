'''Տեքստային ֆայլի համար իրականացնել ծրագիր, 
    որը կհաշվի ֆայլում հանդիպող սիմվոլների քանակը'''

file_name = input("input the file name: ")
fd = open(file_name, 'r')
text = fd.read()
count = 0

for i in text:
    if i.isprintable():
        count += 1

fd.close()
# print(count)