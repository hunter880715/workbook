# coding: GBK 
# 11-1:���к͹��ң���дһ�������������������βΣ�һ����������һ����������
# �����������һ����ʽΪ City, Country ���ַ�����
# 11-2 �˿��������޸ĺ�����ʹ������������ز����ٵ��β� population��
# ����һ����ʽΪ City, Country - population xxx de �ַ�����
# �޸ĺ��������β� population ����Ϊ��ѡ�ġ�
def city_and_country(city, country, population=''):
    """�����������"""
    if population:
        full_show = city + ", " + country + "-" + population
    else:
        full_show = city + ", " + country
    return full_show.title()
