# coding: GBK 
# 10-6 �ӷ����㣺��ʾ�û��ṩ��ֵ����ʱ�������ֵ�һ�������ǣ��û��ṩ�����ı����������֡�
# ����������£����㳢�Խ�����ת��Ϊ֤���ǣ������� ValueError �쳣��
# ��дһ��������ʾ�û������������֣��ٽ�������Ӳ���ӡ�����
# ���û�������κ�һ��ֵ���������Ƕ����� ValueError �쳣������ӡһ���ѺõĴ�����Ϣ��
# �����д�ĳ�����в��ԣ��������������֣�������һЩ�ı����������֡�
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
