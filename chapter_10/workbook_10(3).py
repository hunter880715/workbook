# coding: GBK 
# 10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
# 在这种情况下，当你尝试将输入转换为证书是，将依法 ValueError 异常。
# 编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的任何一个值不是数字是都捕获 ValueError 异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数字，在输入一些文本而不是数字。
try:
    number = input("Give me a number: ")
    number = int(number)
    number_1 = input("Give me another number: ")
    number_1 = int(number_1)
    sum = number + number_1
except ValueError:
    print("Sorry, I really needed a number.")
else:
    print("Sum is: " + str(sum))
