# coding:GBK 
# 8-12 �����Σ���дһ�������������ܹ˿�Ҫ������������ӵ�һϵ��ʳ�ġ�
# �������ֻ��һ���βΣ����ֻ������������ṩ������ʳ�ģ�������ӡһ����Ϣ���Թ˿͵�������ν��и�����
# ��������������Σ�ÿ�ζ��ṩ��ͬ������ʵ�Ρ�
def sandwichs(*toppings):
    """�˿���Ҫ��ʳ��"""
    print(toppings)
sandwichs('����Ѭţ��')
sandwichs('����', '֥ʿ')
sandwichs('����', 'ը������', '������')
# 8-13 �û���飺����ǰ��ĳ��� user_profile.py�������е��� build_profile() ��������ļ�顣
# �����������ʱ��ָ����������գ��Լ�����������ļ�-ֵ�ԡ�
def build_profile(first, last, **user_info):
    """�����Լ��ļ��"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('yulong', 'zhu',
                            domicile='longkou',
                            age='31',
                            stature='181')
print(user_profile)
# 8-14 ��������дһ����������һ����������Ϣ�洢��һ���ֵ��С�
# ����������ǽ��������̺��ͺţ����������������Ĺؼ���ʵ�Ρ�
# ������������������ṩ�ز����ٵ���Ϣ���Լ���������-ֵ�ԣ�����ɫ��ѡװ�����
# ������������ܹ��������������ã�
# car = make_car('subaru', 'outback', color='blue', package=True)
# ��ӡ���ص��ֵ䣬ȷ����ȷ�ش��������е���Ϣ��
def make_car(brand, destination, **car_info):
    """������Ϣ"""
    cars = {}
    cars['brand'] = brand
    cars['destination'] = destination
    for key, value in car_info.items():
        cars[key] = value
    return cars
car = make_car('honda', 'japan',
                color='green',
                tow_package=True)
print(car)    
