# coding: GBK 
# 10-5 关于编程的调查：编写一个 while 循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
filename = r'inquiry.txt'

list_one = []
while True:
    msg = input("Why do you like porgramming?\n")
    list_one.append(msg)
    mess = input("Would you exit(y/n)?")
    if mess == 'y':
        break
        
with open(filename, 'a') as file_objact:
    for list_one in list_one:
        file_objact.write(list_one + "\n")
