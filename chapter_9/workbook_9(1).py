# coding: GBK 
# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。
# 编写一个名为 IceCreamStand 的类，让他集成为完成练习 9-1 或 9-4 而编写的 Restaurant 类。
# 添加一个名为 flavors 的属性，用于存储一个有多种口味冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法，创建 IceCreamStand 实例，并调用这个方法。
class Restaurant():
    """一家餐馆的程序"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆属性"""
        self.name = restaurant_name
        self.type = cuisine_type
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
        self.number_served += additional_servedclass
        
class IceCreamStand(Restaurant):
    """冰淇淋餐馆特殊之处"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # 添加 flavors 属性，建立一个存储种类的列表。

    def show_flavors(self):
        """显示冰淇淋的品种"""
        print("我们提供以下几种口味冰淇淋:")
        for flavors in self.flavors:
            print("- " + flavors.title())

冷饮店名 = IceCreamStand('冰雪皇后', '冷饮')
冷饮店名.flavors = ['vanilla', 'chocolate', 'black cherry']
冷饮店名.describe_restaurant()
冷饮店名.show_flavors()
