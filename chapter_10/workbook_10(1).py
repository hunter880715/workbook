# 10-4 �ÿ���������дһ�� while ��ѭ������ʾ�û����������֡�
# �û��������ֺ�����Ļ�ϴ�ӡһ���ʺ������һ�����ʼ�¼��ӵ��ļ� guest_book.txt �С�
# ȷ������ļ��е�ÿ����¼����ռһ�С�
filename = r'guest_book.txt'
print("\nEnter 'q' exit." )
while True:
    name = input('\nPlease enter in your name: ')
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_objact:
            file_objact.write("\n" + name)
        print("\nHello, " + name)
