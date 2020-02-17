# coding: GBK
# 9-14 ���ӣ�ģ�� random �����Ը��ַ�ʽ����������ĺ�����
# ���� randint() ����һ��λ��ָ����Χ�ڵ�������
# ����һ�� Die �࣬������һ����Ϊ sides �����ԣ������Ե�Ĭ��ֵΪ 6��
# ��дһ����Ϊ roll_die �ķ���������ӡλ�� 1 ����������֮����������
# ����һ����������ӣ����� 10 �Ρ�
# ����һ�� 10 ������Ӻ�һ�� 20 ������ӣ��������Ƕ��� 10 �Ρ�
from random import randint
class Die():
    """������Ϣ"""
    def __init__(self, sides=6):
        """
        ��ʼ������
        ��������Ĭ��ֵΪ 6
        """
        self.sides = sides
        
    def roll_die(self):
        """����һ��λ�� 1 ����������֮��������"""
        return randint(1, self.sides)
        
    
d6 = Die()
d6_list = []
for roll in range(10):
    roll = d6.roll_die()
    d6_list.append(roll)
print(d6_list)

d10 = Die(sides=10)
d10_list = []
for roll in range(10):
    roll = d10.roll_die()
    d10_list.append(roll)
print(d10_list)

d20 = Die(sides=20)
d20_list = []
for roll in range(10):
    roll = d20.roll_die()
    d20_list.append(roll)
print(d20_list)


