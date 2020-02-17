# coding: GBK 
# 9-1 餐馆：创建一个名为 Restaurant 的类，其方法 __init__() 设置两个属性；
# restaurant_namehe 和 cuisine_type 两个属性。
# 创建一个名为 describe_restaurant() 和 open_reataurant() 的方法;
# 其中前者打印前述两项信息，后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印两个属性，在调用前述两个方法。
class Restaurant():
    """一家餐馆的程序"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆属性"""
        self.name = restaurant_name
        self.type = cuisine_type
        # 9-4 就餐人数：创建一个名为 number_served 的属性，并将其默认值设置为0
        self.number_served = 0
        
    def describe_restaurant(self):
        """打印前述两项属性信息"""
        msg = "The restaurant name is: "
        msg += self.name.title() + ";"
        msg += "\n" + "cuisine type is: "
        msg += self.type.title() + ".\n"
        print(msg)
            
    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(self.name.title() + " is on business.\n")
    
    def set_number_served(self, number_served):
        """修改就餐人数"""
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        """就餐人数递增"""
        self.number_served += additional_served
        
restaurant = Restaurant('sunny', 'european') # 创建 restaurant 实例
print(restaurant.name)
print(restaurant.type + '\n')
# 9-4:根据这个类创建一个名为 restaurant 的实例；
# 打印有多少人在这家餐馆就餐过，然后修改这个值并在此打印。
print("Number served: " + str(restaurant.number_served))
restaurant.number_served = 500
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1000)
print("Number served: " + str(restaurant.number_served))
# 9-4 再添加一个名为 increment_number_served() 的方法，它能够将就餐人数递增。
# 调用这个方法并传递一个值：你认为这家餐馆每天可能接待多少名客人。
restaurant.increment_number_served(150)
print("Number served: " + str(restaurant.number_served) + "\n")

restaurant.describe_restaurant() # 调用前述两个方法
restaurant.open_restaurant()
# 9-2 三家餐馆：根据为完成 9-1 练习而编写的类创建三个实例；
# 对每个实例调用方法 describe_restaurant()。
china = Restaurant('china restaurant', 'chinese food')
china.describe_restaurant()

france = Restaurant('france restaurant', 'franch meal')
france.describe_restaurant()

japan = Restaurant('japan restaurant', 'japanese food')
japan.describe_restaurant()
# 9-3 用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name 以及通常常用属性；
# 在类 User 中定义一个名为 describe_user() 的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user() 的方法，它向用户发出个性化问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    """个人信息"""
    def __init__(self, first_name, last_name, age, height, marriage):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.marriage = marriage
    
    def describe_user(self):
        """信息打印"""
        msg = "First name: " + self.first.title() + "\n"
        msg += "Last name: " + self.last.title() + "\n"
        msg += "Age: " + str(self.age) + "\n"
        msg += "Height: " + str(self.height) + "cm\n"
        msg += "Marriage: " + self.marriage.title() + "\n"
        print(msg)
            
    def greet_user(self):
        """简单问候"""
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
