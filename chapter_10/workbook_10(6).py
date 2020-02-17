# coding:GBK 
# 10-11 喜欢的数字：编写一个程序，提示用户输入它喜欢的数字；
# 使用 json.dump() 将这个数字存储到文件中。
import json

filename = 'numbers.json'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
