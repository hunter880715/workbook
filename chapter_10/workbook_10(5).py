# coding: GBK 
# 10-8 è�͹������������ļ� cats.txt �� dogs.txt��
# �ڵ�һ���ļ������ٴ洢��ֻè�����֣��ڵڶ����ļ������ٴ洢��ֻ�������֡�
# ��дһ�����򣬳��Զ�ȡ��Щ�ļ����������е����ݴ�ӡ����Ļ�ϡ�
# ����Щ�������һ�� try-except ������У��Ա����ļ�������ʱ���� FileNotError ���󣬲���ӡһ���Ѻ���Ϣ��
# ������һ���ļ�һ����һ���ط�����ȷ�� except ������еĴ��뽫��ȷ��ִ�С�
filename = ['cats.txt', 'dogs.txt']
for filename in filename:
    print(filename + ":")
    try:
        with open(filename) as f:
            f = f.read().title()
            print(f)
    except FileNotFoundError:
        print("- Sorry, I can't find that file.\n")
# 10-9 ��Ĭ��è�͹����޸� 10-8 ��д�� except ����飬�ó������ļ�������ʱһ�Բ�����
filename = ['cats.txt', 'dogs.txt']
for filename in filename:
    try:
        with open(filename) as f:
            f = f.read().title()
    except FileNotFoundError:
        pass
    else:
        print(filename + ":")
        print(f)
# 10-10 �������ʣ�������Ŀ Gutenberg������һЩ���������ͼ�顣
# ������Щ��Ʒ���ı��ļ���������е�ԭʼ�ı����Ƶ��ı��ļ��С�
# �����ʹ�÷��� count() ��ȷ���ض��ĵ��ʻ�������ַ����г����˶��ٴΡ�
# ���磺
line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')
# ͨ��ʹ�� lower() ���ַ���ת��ΪСд���ɲ�׽Ҫ���ҵĵ��ʳ��ֵ����д��������������Сд��ʽ��Ρ�
# ��дһ����������ȡ������Ŀ Gutenberg �л�ȡ���ļ���
# ���㵥��"the"��ÿ���ļ��зֱ�����˶��ٴΡ�
def count_words(filename):
    """�����ĵ��ж��ٸ���"""
    try:
        with open(filename) as f_obj:
            f_obj = f_obj.read()
    except FileNotFoundError:
        mess = "Sorry, the file " + filename + "does not exist."
        print(mess)
    else:
        # ���㵥��'the'���ļ��г����˶��ٴ�
        words = f_obj.count('the')
        
        print("The file " + filename + " has about " + 
            str(words) + " words.")
        # �����ĵ��ڵ��ʵ��ж���
    else:
        words = f_obj.split()
        word = len(words)
        print("The file " + filename + " has about " + 
            str(word) + "words.")

filename = r'zhijiage1990.txt'
count_words(filename)
