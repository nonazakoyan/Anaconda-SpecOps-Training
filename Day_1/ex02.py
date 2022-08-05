'''Տրված ֆայլում պարունակվում է տեքստ։ 
    Իրականացնել ծրագիր, որը ֆայլի մեջ պարունակվող տեքստի  
    բոլոր բառերի առաջին տառերը դարձնում է մեծատառ և 
    ձևափոխված ամբողջ տեքստը պահպանում մեկ այլ ֆայլում։'''

file_name = input("input the file name: ")

fd = open(file_name, 'r')
text = fd.read().strip()

fd1 = open("output.txt", "w")
fd1.write(text.title())
fd.close()
fd1.close()