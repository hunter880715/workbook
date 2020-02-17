# coding: GBK 
# 10-3 访客：编写一个程序，提示用户输入其名字；用户做出响应后，将其名字写入到文件 guest.txt 中。
name = input('\nPlease enter in your name: ')
filename = r'guest.txt'
with open(filename, 'w') as file_objact:
    file_objact.write(name)
