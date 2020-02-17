# coding:GBK 
# 10-12 ��סϲ�������֣�����ϵ 10-11 �е���������϶�Ϊһ��
# ����洢���û�ϲ�������֣������û���ʾ����������ʾ�û�������ϲ�������ֲ�����洢���ļ��С�
# ��������������Σ��������Ƿ���Ԥ������������
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
