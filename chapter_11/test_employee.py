# coding: GBK 
# ʹ�÷��� setUp()��������ÿ�����Է����ж������µĹ�Աʵ����
# �����������������ȷ���������Զ�ͨ���ˡ�
import unittest
from workbook_11 import *
class TestEmployee(unittest.TestCase):
    """���Employee��Ĳ���"""
    
    def setUp(self):
        """����һ��Employeeʵ�����Ա��ڲ�����ʹ�á�"""
        self.zhu = Employee('yulong', 'zhu', 65000)

    def test_give_default_raise(self):
        """����ʹ��Ĭ�ϵ���н�������Ƿ���С�"""
        self.zhu.give_raise()
        self.assertEqual(self.zhu.salary, 70000)

    def test_give_custom_raise(self):
        """�����Զ�����н�������Ƿ���С�"""
        self.zhu.give_raise(10000)
        self.assertEqual(self.zhu.salary, 75000)
        
unittest.main()
