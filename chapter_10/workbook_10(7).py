# coding:GBK 
# 10-12 记住喜欢的数字：将联系 10-11 中的两个程序合而为一。
# 如果存储了用户喜欢的数字，就像用户显示他，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期那样工作。
import json

filename = 'numbers_1.json'
try:
    with open(filename) as f_obj:
        numbers_1 = json.load(f_obj)
except FileNotFoundError:
    numbers_1 = input("Please enter your favorite numbers: ")
    with open(filename,'w') as f_obj:
        json.dump(numbers_1, f_obj)
else:
    mess = "I know your favorite number! It's: "
    print(mess + str(list(numbers_1)) + ".\n" )
