# coding:GBK 
# ��дһ�����򣬴��ļ��ж�ȡ���ֵ������ӡ��Ϣ"I know your favorite number! It's: ."��
import json

filename = 'numbers.json'
with open(filename) as f_job:
    numbers = json.load(f_job)

msg = "I know your favorite number! It's: "
print(msg + str(list(numbers)) + ".\n")
