# coding: GBK 
# 9-12 ����һ���ļ��������д���һ�� Admin ��ʵ����
# ������÷��� show_privileges����ȷ��һ�ж���Ȼ�ܹ���ȷ�����С�
from user import User
from admin import Admin, Privileges

zhu = Admin('yulong', 'zhu', 31, 181, 'no')
zhu.describe_user()

zhu_1 = ['can add port', 'can delete port', 'can ban user']
zhu.privileges.privileges = zhu_1
zhu.privileges.show_privileges()
