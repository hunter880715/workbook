# coding:GBK 
# 9-10 导入 Restaurant 类，创建一个 Restaurant 实例；
# 调用 Restaurant 的一个方法，以确认 import 语句正确无误。
from restaurant import Restaurant, IceCreamStand

my_rest = Restaurant('alibaba', 'chinese food')
my_rest.describe_restaurant()

my_ice = IceCreamStand('king s', 'coolers')
my_ice.flavors = ['cheese', 'beurre', 'nut fruit']
my_ice.describe_restaurant()
my_ice.show_flavors()
