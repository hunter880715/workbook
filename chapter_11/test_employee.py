# coding: GBK 
# 使用方法 setUp()，以免在每个测试方法中都创建新的雇员实例。
# 运行这个测试用例，确认两个测试都通过了。
import unittest
from workbook_11 import *
class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    
    def setUp(self):
        """创建一个Employee实例，以便在测试中使用。"""
        self.zhu = Employee('yulong', 'zhu', 65000)

    def test_give_default_raise(self):
        """测试使用默认的年薪增加量是否可行。"""
        self.zhu.give_raise()
        self.assertEqual(self.zhu.salary, 70000)

    def test_give_custom_raise(self):
        """测试自定义年薪增加量是否可行。"""
        self.zhu.give_raise(10000)
        self.assertEqual(self.zhu.salary, 75000)
        
unittest.main()
