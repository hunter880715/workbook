# coding: GBK 
# 9-10 导入 Restaurant 类：将最新的 Restaurant 类春出在一个模块中。
"""一个可以用于表示餐馆各种属性的类"""
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
