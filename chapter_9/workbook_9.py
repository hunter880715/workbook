# coding: GBK 
# 9-1 �͹ݣ�����һ����Ϊ Restaurant ���࣬�䷽�� __init__() �����������ԣ�
# restaurant_namehe �� cuisine_type �������ԡ�
# ����һ����Ϊ describe_restaurant() �� open_reataurant() �ķ���;
# ����ǰ�ߴ�ӡǰ��������Ϣ�����ߴ�ӡһ����Ϣ��ָ���͹�����Ӫҵ��
# ��������ഴ��һ����Ϊ restaurant ��ʵ�����ֱ��ӡ�������ԣ��ڵ���ǰ������������
class Restaurant():
    """һ�Ҳ͹ݵĳ���"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """��ʼ���͹�����"""
        self.name = restaurant_name
        self.type = cuisine_type
        # 9-4 �Ͳ�����������һ����Ϊ number_served �����ԣ�������Ĭ��ֵ����Ϊ0
        self.number_served = 0
        
    def describe_restaurant(self):
        """��ӡǰ������������Ϣ"""
        msg = "The restaurant name is: "
        msg += self.name.title() + ";"
        msg += "\n" + "cuisine type is: "
        msg += self.type.title() + ".\n"
        print(msg)
            
    def open_restaurant(self):
        """ָ���͹�����Ӫҵ"""
        print(self.name.title() + " is on business.\n")
    
    def set_number_served(self, number_served):
        """�޸ľͲ�����"""
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        """�Ͳ���������"""
        self.number_served += additional_served
        
restaurant = Restaurant('sunny', 'european') # ���� restaurant ʵ��
print(restaurant.name)
print(restaurant.type + '\n')
# 9-4:��������ഴ��һ����Ϊ restaurant ��ʵ����
# ��ӡ�ж���������Ҳ͹ݾͲ͹���Ȼ���޸����ֵ���ڴ˴�ӡ��
print("Number served: " + str(restaurant.number_served))
restaurant.number_served = 500
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1000)
print("Number served: " + str(restaurant.number_served))
# 9-4 �����һ����Ϊ increment_number_served() �ķ��������ܹ����Ͳ�����������
# �����������������һ��ֵ������Ϊ��Ҳ͹�ÿ����ܽӴ����������ˡ�
restaurant.increment_number_served(150)
print("Number served: " + str(restaurant.number_served) + "\n")

restaurant.describe_restaurant() # ����ǰ����������
restaurant.open_restaurant()
# 9-2 ���Ҳ͹ݣ�����Ϊ��� 9-1 ��ϰ����д���ഴ������ʵ����
# ��ÿ��ʵ�����÷��� describe_restaurant()��
china = Restaurant('china restaurant', 'chinese food')
china.describe_restaurant()

france = Restaurant('france restaurant', 'franch meal')
france.describe_restaurant()

japan = Restaurant('japan restaurant', 'japanese food')
japan.describe_restaurant()
# 9-3 �û�������һ����Ϊ User ���࣬���а������� first_name �� last_name �Լ�ͨ���������ԣ�
# ���� User �ж���һ����Ϊ describe_user() �ķ���������ӡ�û���ϢժҪ��
# �ٶ���һ����Ϊ greet_user() �ķ����������û��������Ի��ʺ�
# ���������ʾ��ͬ�û���ʵ��������ÿ��ʵ����������������������
class User():
    """������Ϣ"""
    def __init__(self, first_name, last_name, age, height, marriage):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.marriage = marriage
    
    def describe_user(self):
        """��Ϣ��ӡ"""
        msg = "First name: " + self.first.title() + "\n"
        msg += "Last name: " + self.last.title() + "\n"
        msg += "Age: " + str(self.age) + "\n"
        msg += "Height: " + str(self.height) + "cm\n"
        msg += "Marriage: " + self.marriage.title() + "\n"
        print(msg)
            
    def greet_user(self):
        """���ʺ�"""
        full_name = self.first + " " + self.last
        print("Hello, " + full_name.title() + ", how do you do?\n")
        
zhang = User('wuji', 'zhang', 21, 176, 'yes')
zhang.describe_user()
zhang.greet_user()

lee = User('xunhuan', 'lee', 33, 179, 'yes')
lee.describe_user()
lee.greet_user()

zhu = User('yulong', 'zhu', 31, 181, 'no')
zhu.describe_user()
zhu.greet_user()
