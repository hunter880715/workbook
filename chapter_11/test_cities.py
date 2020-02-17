# coding: GBK 
# �Ժ��� city_and_country() ���в��ԣ��ǵõ���ģ�� unittest �Լ�Ҫ���Եĺ�������
# ��дһ����Ϊ test_city_country() �ķ�������ʵʹ��������'sabtuage'��'chile'������ֵ�����ú���ʱ���õ����ַ�������ȷ�ġ�
# ���� test_cities.py��ȷ�ϲ��� test_city_country() ͨ���ˡ�
# ��дһ����Ϊ test_city_country_population() �Ĳ��ԣ���������������ٴ�����test_cities.py��
# ȷ�� test_city_country_population() ͨ���ˡ�
import unittest
from city_functions import city_and_country

class CitysTestCase(unittest.TestCase):
    """����test_ciries.py"""
    
    def test_city_country(self):
        """�����ܷ��ܹ�����������͹�����������ֵ"""
        c_and_c = city_and_country('shang hai', 'china')
        self.assertEqual(c_and_c, 'Shang Hai, China')
        
    def test_city_country_population(self):
        """�����ܷ���������͹������Լ��˿�����"""
        full_show = city_and_country(
                'long kou',
                'china',
                'population=600000')
        self.assertEqual(full_show, 'Long Kou, China-Population=600000')
        
unittest.main()
