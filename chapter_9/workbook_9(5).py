# coding: GBK 
# 9-13 ʹ�� OrderedDict��
from collections import OrderedDict

glossaries = OrderedDict()
glossaries['print'] = '��ӡ��Ϣ'
glossaries['for'] = 'ѭ�����'
glossaries['del'] = 'ɾ��Ԫ��'
glossaries['if'] = '��֧���'
glossaries['set'] = '����'

for key, value in glossaries.items():
    print(key.title() + ": " + value.title() + "\n")
