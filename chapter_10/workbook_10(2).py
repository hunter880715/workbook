# coding: GBK 
# 10-5 ���ڱ�̵ĵ��飺��дһ�� while ѭ����ѯ���û�Ϊ��ϲ����̡�
# ÿ���û�����һ��ԭ��󣬶�������ӵ�һ���洢����ԭ����ļ��С�
filename = r'inquiry.txt'

list_one = []
while True:
    msg = input("Why do you like porgramming?\n")
    list_one.append(msg)
    mess = input("Would you exit(y/n)?")
    if mess == 'y':
        break
        
with open(filename, 'a') as file_objact:
    for list_one in list_one:
        file_objact.write(list_one + "\n")
