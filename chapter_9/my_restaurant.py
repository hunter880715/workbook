# coding:GBK 
# 9-10 ���� Restaurant �࣬����һ�� Restaurant ʵ����
# ���� Restaurant ��һ����������ȷ�� import �����ȷ����
from restaurant import Restaurant, IceCreamStand

my_rest = Restaurant('alibaba', 'chinese food')
my_rest.describe_restaurant()

my_ice = IceCreamStand('king s', 'coolers')
my_ice.flavors = ['cheese', 'beurre', 'nut fruit']
my_ice.describe_restaurant()
my_ice.show_flavors()
