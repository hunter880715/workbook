# coding:GBK 
# 8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。
# 这个函数只有一个形参（它手机函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概括。
# 调用这个函数三次，每次懂提供不同数量的实参。
def sandwichs(*toppings):
    """顾客需要的食材"""
    print(toppings)
sandwichs('五香熏牛肉')
sandwichs('番茄', '芝士')
sandwichs('生菜', '炸鸡胸肉', '甜辣酱')
# 8-13 用户简介：复制前面的程序 user_profile.py，在其中调用 build_profile() 来创建你的简介。
# 调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
def build_profile(first, last, **user_info):
    """属于自己的简介"""
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
# 8-14 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可少的信息，以及两个名称-值对，如颜色和选装配件。
# 这个函数必须能够像下面这样调用：
# car = make_car('subaru', 'outback', color='blue', package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(brand, destination, **car_info):
    """汽车信息"""
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
