# coding: GBK
# 10-7 加法计算器：将为完成练习 10-6 而编写的代码放在一个 while 循环中；
# 让用户犯错（输入的是文本而不是数字）后，能够继续输入数字。
print("(Enter 'q' exit.)")
while True:
    x = input("Give me a number: ")
    if x == 'q':
        break
    y = input("Give me another number: ")
    if y == 'q':
        break
    try:
        sum = int(x) + int(y)
    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        print("Sum is: " + str(sum))
