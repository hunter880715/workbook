# coding: GBK 
# 9-13 使用 OrderedDict：
from collections import OrderedDict

glossaries = OrderedDict()
glossaries['print'] = '打印信息'
glossaries['for'] = '循环语句'
glossaries['del'] = '删除元素'
glossaries['if'] = '分支语句'
glossaries['set'] = '集合'

for key, value in glossaries.items():
    print(key.title() + ": " + value.title() + "\n")
