# coding: GBK
# 10-7 �ӷ�����������Ϊ�����ϰ 10-6 ����д�Ĵ������һ�� while ѭ���У�
# ���û�������������ı����������֣����ܹ������������֡�
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
