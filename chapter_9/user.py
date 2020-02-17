# coding: GBK 
# 9-11 导入 Admin 类：以练习 9-8 为基础，将 User、Privileges 和 Admin 类存储在一个模块中。
"""一个关于用户属性的类"""
class User():
    """个人信息"""
    def __init__(self, first_name, last_name, age, height, marriage):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.marriage = marriage
        self.login_attempts = 0
    
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
        
    def increment_login_attempts(self):
        """将属性 login_attempts 的值加 1 """
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """将属性 login_attempts 的值归零"""
        self.login_attempts = 0
