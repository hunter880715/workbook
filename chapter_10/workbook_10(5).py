# coding: GBK 
# 10-8 猫和狗：创建两个文件 cats.txt 和 dogs.txt；
# 在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三只狗的名字。
# 编写一个程序，尝试读取这些文件，并将其中的内容打印到屏幕上。
# 将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotError 错误，并打印一条友好消息。
# 将其中一个文件一道另一个地方，并确认 except 代码块中的代码将正确的执行。
filename = ['cats.txt', 'dogs.txt']
for filename in filename:
    print(filename + ":")
    try:
        with open(filename) as f:
            f = f.read().title()
            print(f)
    except FileNotFoundError:
        print("- Sorry, I can't find that file.\n")
# 10-9 沉默的猫和狗：修改 10-8 编写的 except 代码块，让程序在文件不存在时一言不发。
filename = ['cats.txt', 'dogs.txt']
for filename in filename:
    try:
        with open(filename) as f:
            f = f.read().title()
    except FileNotFoundError:
        pass
    else:
        print(filename + ":")
        print(f)
# 10-10 常见单词：访问项目 Gutenberg，并找一些逆向分析的图书。
# 下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法 count() 来确定特定的单词或短语在字符串中出现了多少次。
# 例如：
line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')
# 通过使用 lower() 将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。
# 编写一个程序，他读取你在项目 Gutenberg 中获取的文件；
# 计算单词"the"在每个文件中分别出现了多少次。
def count_words(filename):
    """计算文档有多少个字"""
    try:
        with open(filename) as f_obj:
            f_obj = f_obj.read()
    except FileNotFoundError:
        mess = "Sorry, the file " + filename + "does not exist."
        print(mess)
    else:
        # 计算单词'the'在文件中出现了多少次
        words = f_obj.count('the')
        
        print("The file " + filename + " has about " + 
            str(words) + " words.")
        # 计算文档内单词的有多少
    else:
        words = f_obj.split()
        word = len(words)
        print("The file " + filename + " has about " + 
            str(word) + "words.")

filename = r'zhijiage1990.txt'
count_words(filename)
