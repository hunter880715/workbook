# coding: GBK 
# 10-1 Python ѧϰ�ʼǣ����ı��༭�����½�һ���ļ���д��������ܽ�һ��������ѧ���� Python ֪ʶ��
# ������ļ�����Ϊ learning_python.txt��������洢��Ϊ������ϰ����д�ĳ������ڵ�Ŀ¼�С�
# ��дһ����������ȡ����ļ�����������д�����ݴ�ӡ���Σ�
# ��һ�δ�ӡ�Ҷ�ȡ�����ļ����ڶ��δ�ӡʱ�����ļ�����
# �����δ�ӡʱ�����д洢��һ���б��У����� with ��������ӡ���ǡ�
with open('learning_python.txt') as learn:
    learn = learn.read()
    print(learn.rstrip() + '\n')      # ��һ�δ�ӡ����ȡ�����ļ�
    
learning = r'learning_python.txt'
with open(learning) as learn:
    for learn in learn:
        print(learn.rstrip() + '\n')  # �ڶ��δ�ӡ�������ļ�����
        
learning = r'learning_python.txt'
with open(learning) as learn:
    learn = learn.readlines()
    for learn in learn:
        print(learn.strip() + '\n')   # �����δ�ӡ�������д洢��һ���б���
        
# 10-2 C����ѧϰ�ʼǣ���ʹ�÷��� replace() ���ַ����е��ض����ʶ��滻Ϊ��һ�����ʡ�
# ��ȡ��մ������ļ� learning_python.txt �е�ÿһ�У������е� Python ���滻Ϊ C��
# ���޸ĺ�ĸ��ж���ӡ����Ļ�ϡ�
learning = r'learning_python.txt'
with open(learning) as learn:
    learn = learn.readlines()
    for learn in learn:
        learn = learn.rstrip()
        print(learn.replace('Python', 'C'))
        
