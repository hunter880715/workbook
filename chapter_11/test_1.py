import unittest
from workbook_11 import *

class TestEmployee(unittest.TestCase):
    
    def test_one(self):
        self.zhu = Employee('zheng', 'zhu', 10000)
        self.zhu.give_raise()
        self.assertEqual(self.zhu.Employee, 'Zheng, Zhu, 11000')
        
unittest.main()
