# coding: GBK
# Ϊ Employee ��дһ���������������а����������Է���;
# test_give_default_raise()��test_give_custom_raise()��
# ���в���������ȷ���������������ˡ�
import unittest
from workbook_11 import *

class TestEmployee(unittest.TestCase):
    """���Employee��Ĳ���"""
    
    def test_give_default_raise(self):
        """����ʹ��Ĭ�ϵ���н�������Ƿ���С�"""
        self.zhu = Employee('yulong', 'zhu', 15000)
        self.zhu.give_raise()
        self.assertEqual(self.zhu.salary, 20000)
        
    def test_give_custom_raise(self):
        self.zhu = Employee('yulong', 'zhu', 15000)
        self.zhu.give_raise(10000)
        self.assertEqual(self.zhu.salary, 25000)
        
unittest.main()
