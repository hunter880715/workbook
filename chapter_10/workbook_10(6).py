# coding:GBK 
# 10-11 ϲ�������֣���дһ��������ʾ�û�������ϲ�������֣�
# ʹ�� json.dump() ��������ִ洢���ļ��С�
import json

filename = 'numbers.json'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
