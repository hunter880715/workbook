# 10-4 访客名单：编写一个 while 的循环，提示用户输入其名字。
# 用户输入名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。
# 确保这个文件中的每条记录都独占一行。
filename = r'guest_book.txt'
print("\nEnter 'q' exit." )
while True:
    name = input('\nPlease enter in your name: ')
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_objact:
            file_objact.write("\n" + name)
        print("\nHello, " + name)
