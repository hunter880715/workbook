# coding: GBK
# 为 Employee 编写一个测试用例，其中包含两个测试方法;
# test_give_default_raise()和test_give_custom_raise()。
# 运行测试用例，确认两个方法都过了。
import unittest
from workbook_11 import *

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    
    def test_give_default_raise(self):
        """测试使用默认的年薪增加量是否可行。"""
        self.zhu = Employee('yulong', 'zhu', 15000)
        self.zhu.give_raise()
        self.assertEqual(self.zhu.salary, 20000)
        
    def test_give_custom_raise(self):
        self.zhu = Employee('yulong', 'zhu', 15000)
        self.zhu.give_raise(10000)
        self.assertEqual(self.zhu.salary, 25000)
        
unittest.main()
