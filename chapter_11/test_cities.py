# coding: GBK 
# 对函数 city_and_country() 进行测试（记得导入模块 unittest 以及要测试的函数）。
# 编写一个名为 test_city_country() 的方法，核实使用类似于'sabtuage'和'chile'这样的值来调用函数时，得到的字符串是正确的。
# 运行 test_cities.py，确认测试 test_city_country() 通过了。
# 编写一个名为 test_city_country_population() 的测试，调用这个函数，再次运行test_cities.py；
# 确认 test_city_country_population() 通过了。
import unittest
from city_functions import city_and_country

class CitysTestCase(unittest.TestCase):
    """测试test_ciries.py"""
    
    def test_city_country(self):
        """测试能否能够处理城市名和国家名这样的值"""
        c_and_c = city_and_country('shang hai', 'china')
        self.assertEqual(c_and_c, 'Shang Hai, China')
        
    def test_city_country_population(self):
        """测试能否处理城市名和国家名以及人口数量"""
        full_show = city_and_country(
                'long kou',
                'china',
                'population=600000')
        self.assertEqual(full_show, 'Long Kou, China-Population=600000')
        
unittest.main()
