# coding: GBK 
# 10-3 �ÿͣ���дһ��������ʾ�û����������֣��û�������Ӧ�󣬽�������д�뵽�ļ� guest.txt �С�
name = input('\nPlease enter in your name: ')
filename = r'guest.txt'
with open(filename, 'w') as file_objact:
    file_objact.write(name)
