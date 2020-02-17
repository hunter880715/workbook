# coding: GBK 
# 10-1 Python 学习笔记：在文本编辑器中新建一个文件，写几句后来总结一下你至此学到的 Python 知识。
# 将这个文件命名为 learning_python.txt，并将其存储到为本章练习而编写的程序所在的目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次；
# 第一次打印室读取整个文件；第二次打印时遍历文件对象；
# 第三次打印时将各行存储在一个列表中，再在 with 代码块外打印它们。
with open('learning_python.txt') as learn:
    learn = learn.read()
    print(learn.rstrip() + '\n')      # 第一次打印：读取整个文件
    
learning = r'learning_python.txt'
with open(learning) as learn:
    for learn in learn:
        print(learn.rstrip() + '\n')  # 第二次打印：遍历文件对象
        
learning = r'learning_python.txt'
with open(learning) as learn:
    learn = learn.readlines()
    for learn in learn:
        print(learn.strip() + '\n')   # 第三次打印：将各行存储在一个列表中
        
# 10-2 C语言学习笔记：可使用方法 replace() 将字符串中的特定单词都替换为另一个单词。
# 读取你刚创建的文件 learning_python.txt 中的每一行，将其中的 Python 都替换为 C；
# 将修改后的各行都打印到屏幕上。
learning = r'learning_python.txt'
with open(learning) as learn:
    learn = learn.readlines()
    for learn in learn:
        learn = learn.rstrip()
        print(learn.replace('Python', 'C'))
        
