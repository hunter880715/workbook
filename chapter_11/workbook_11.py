# coding: GBK 
# 11-3 ��Ա����дһ����Ϊ Employee ���࣬�䷽��__init__()���������պ���н���������Ƕ��洢�������С�
# ��дһ����Ϊ give_raise() �ķ�������Ĭ�Ͻ���н���� 5000 ��Ԫ����Ҳ�ܹ�������������н���ӡ�
class Employee():
    """��Ա����Ϣ"""
    
    def __init__(self, first, last, salary):
        """��ʼ������"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """Ĭ������нˮ5000"""
        self.salary += amount
