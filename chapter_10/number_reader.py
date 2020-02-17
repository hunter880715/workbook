# coding:GBK 
# 编写一个程序，从文件中读取这个值，并打印消息"I know your favorite number! It's: ."。
import json

filename = 'numbers.json'
with open(filename) as f_job:
    numbers = json.load(f_job)

msg = "I know your favorite number! It's: "
print(msg + str(list(numbers)) + ".\n")
