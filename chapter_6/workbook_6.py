# coding: GBK 
# 6-1 ʹ��һ���ֵ����洢һ�����˵���Ϣ�����������ա�����;�ס�ĳ��С�
# ���ֵ�Ӧ�������� first_name, last_name, age �� city.
# ���洢���ֵ��е�ÿ����Ϣ����ӡ������
personal_data = {
    'first_name':'hunter',
    'last_name':'zhu',
    'age':'31',
    'city':'yantai',
    }
for key, value in personal_data.items():     # ��ȡ items() ��ѭ���Ĵ�ӡ������
    print(key.title() +": " + value.title())
# ��ͨ��ʽ��ӡ��    
print("First name: " + personal_data['first_name'].title())
print("Last name: " + personal_data['last_name'].title())
print("Age: " + personal_data['age'])
print("Habitable city: " + personal_data['city'].title() + "\n")
# 6-2 ϲ�������֣�ʹ��һ���ֵ�洢һЩ��ϲ�������֡�
# �������˵����֣�������Щ���������ֵ��еļ���
# ��ӡÿ���˵����ֺ�ϲ�������֡�
favorite_number = {
    'zhao': 19,
    'qian': 22,
    'sun': 12,
    'lee': 30,
    'wu': 7,
    }
for name, number in favorite_number.items():  # ��ȡ times() ��ѭ���Ĵ�ӡ������
    print(name.title() + 
    "'s favorite number is: " + str(number) + ".\n")
# ��ͨ��ӡ������
print("Zhao's favorite number is " + str(favorite_number['zhao']) + ".\n")
print("Qian's favorite number is " + str(favorite_number['qian']) + ".\n")
print("Sun's favorite number is " + str(favorite_number['sun']) + ".\n")
print("Lee's favorite number is " + str(favorite_number['lee']) + ".\n")
print("Wu's favorite number is " + str(favorite_number['wu']) + ".\n")
# 6-3 �ʻ��Python �ֵ������ģ����ʵ�����е��ֵ䣬��Ϊ������������ǽ����߳�Ϊ���ʻ����
# �����ǰ��ѧ���� 5 ����̴ʻ㣬�����������ʻ���еļ����������ǵĺ�����Ϊֵ�洢�ڴʻ���С�
# ������ķ�ʽ��ӡÿ���ʻ㼰�京�壻
# ������һ�д�ӡ�ʻ㣬��ʹ�û��з�����һ�����У��ú�����һ���������ķ�ʽ��ӡ�ʻ�ĺ��塣
glossaries = {
    'print': '��ӡ��Ϣ',
    'for': 'ѭ�����',
    'if': '��֧���',
    'else': '��ת',
    'del': 'ɾ��Ԫ��'
    }
print("print: \n" + "\t" + glossaries['print'])
print("for: \n" + "\t" + glossaries['for'])
print("if: \n" + "\t" + glossaries['if'])
print("else: \n" + "\t" + glossaries['else'])
print("del: \n" + "\t" + glossaries['del'] + "\n")
# 6-4 �ʻ�� 2���� 6-3 Ϊ��ϰ��д�Ĵ��룬������һϵ������滻Ϊһ�������ֵ��еļ���ֵ��ѭ����
# ȷ��ѭ����������ڴʻ������� 5 �� Python ����������
glossaries = {
    'print': '��ӡ��Ϣ',
    'for': 'ѭ�����',
    'if': '��֧���',
    'slse': '��ת',
    'del': 'ɾ��Ԫ��',
    'py': 'Python',
    'set()': '����',
    'items()': '����һ����-ֵ���б�',
    'keys()': 'ֻ��ȡ��',
    'values()': 'ֻ��ȡֵ'
    }
for key, value in glossaries.items():
    print('key: ' + key + '\n')
    print('value: ' + value + '\n')
# 6-5 ����������һ���ֵ䣬�����д洢�������������2�����Ĺ��ҡ�
# ʹ��ѭ��Ϊÿ��������ӡһ����Ϣ����"The Nile runs through Egypt."��
rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'amazon': 'brazil',
    }
for key, value in rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title() + '.\n')
for river in rivers.keys():    # ʹ��ѭ�������ֵ���ÿ�����������ֶ���ӡ������
    print(river.title() + '\n')
for river in rivers.values():  # ʹ��ѭ�������ֵ��а�����ÿ���������ֶ���ӡ������
    print(river.title() + '\n')
# 6-6 ���飺�� 6.3.1 �ڱ�д�ĳ��� favorite_languages.py ��ִ�����²�����
# ����һ��Ӧ�û���ܵ������Ա������������Щ���Ѿ��������ֵ��У���������δ�������ֵ��С�
# ���������Ա�����������Ѳ��������˴�ӡһ����Ϣ��л����δ���������˴�ӡ��Ϣ������顣
favorite_languagse = {
    'jen': 'pthong',
    'sarah': 'c',
    'edward': 'ruby',
    }
friends = ['jam','jen','sarah','saru','edward']
for name in friends:
    if name in favorite_languagse.keys():
        print(name.title() + ",think you!\n")
    else:
        print(name.title() + ",please take our poll.\n")
# 6-7 �ˣ���Ϊ�����ϰ 6-1 ����д�ĳ����У��ڴ���������ʾ�˵��ֵ䣻
# ���������ֵ䶼�洢��һ����Ϊ people ���б��С�
# ��������б�������ÿ���˵�������Ϣ����ӡ������
fmily_0 = {
    'first_name': 'yulong',
    'last_name': 'zhu',
    'age': 31,
    'city': 'longkou',
    }
fmily_1 = {
    'first_name': 'yan',
    'last_name': 'xu',
    'age': 62,
    'city': 'longkou',
    }
fmily_2 = {
    'first_name': 'xue',
    'last_name': 'zhu',
    'age': 38,
    'city': 'laiyang',
    }
people = [fmily_0, fmily_1, fmily_2]
for people in people:
    print(people)
    print('first name: ' + people['first_name'].title())
    print('last name: ' + people['last_name'].title())
    print('age: ' + str(people['age']))
    print('city: ' + people['city'].title() + '\n')
    
# 6-8 ��������ֵ䣬����ÿ���ֵ䣬��ʹ��һ�����������������������
# ��ÿ���ֵ��У�������������ͼ������˵����֡�
# ����Щ�ֵ�洢��һ����Ϊ pets ���б��У��ڱ������б����������������Ϣ����ӡ������
wang = {
    'species': 'dog',
    'owner': 'tom',
    }
miao = {
    'species': 'cat',
    'owner': 'jack',
    }
qiou = {
    'species': 'bird',
    'owner': 'devid',
    }
pets = [wang, miao, qiou]
for pet in pets:
    print('\n' + 'spevies: ' + pet['species'].title())
    print('owner: ' + pet['owner'].title())
# 6-9 ϲ���ĵط�������һ����Ϊ favorite_places ���ֵ䣬������ֵ��У��������˵�������Ϊ����
# �������е�ÿ���ˣ����洢��ϲ���� 1~3 ���ط���
# ��������ֵ䣬��������ÿ���˵����ּ���ϲ���ĵط���ӡ������
favorite_places = {
    'wang': ['xinjiang', 'shanghai'],
    'zhang': ['shanghai','xian'],
    'lee': ['beijing', 'qingdao', 'weihai'],
    }

for name, place in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in place:
        print("\t" + place.title())
# 6-10 ϲ�������֣��޸�Ϊ��� 6-2 ����д�ĳ�����ÿ���˶������ж��ϲ�������֣�
# ��ÿ���˵����ּ���ϲ�������ִ�ӡ������
favorite_number = {
    'zhao': [3, 19],
    'qian': [12, 24, 44],
    'sun': [1, 8, 45],
    'lee': [4, 30],
    'wu': [7, 27],
    }
for name, numbers in favorite_number.items():
    print("\n" + name.title() + "'s favorote numbers are: ")
    for number in numbers:
        print("\t" + str(number))
# 6-11 ���У�����һ����Ϊ cities ���ֵ䣬���н�������������������
# ����ÿ�����ж�����һ���ֵ䣬�������а����ó��������� ���ҡ��˿�Լ���Լ�һ���йص���ʵ��
# �ڱ�ʾÿ�����е��ֵ��У�Ӧ���� country��population �� fact �ȼ���
# ��ÿ�����е������Լ��й����ǵ���Ϣ����ӡ������
cities = {
    'new york': {
        'country': 'america',
        'population': 8510000,
        'fact': 'economic center',
        },
    'shanghai': {
        'country': 'china',
        'population': 24240000,
        'fact': 'flourshing',
        },
    'aleppo': {
        'country': 'syria',
        'population': 2300000,
        'fact': 'civil war',
        },
    }
for cityname, city_info in cities.items():
    print('\n' + 'cityname: ' + cityname.title())
    # ���������ʽ��
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print('\t' + "country: " + country.title())
    print('\t' + "population: " + str(population))
    print('\t' + "fact: " + fact)
    # �Ľ������ʽ��
    for key, value in city_info.items():
        print('\t' + key.title() + ': ' + str(value))
