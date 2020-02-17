# coding: GBK 
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

# 9-7 管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承 9-5 练习编写的 User 类。
# 添加一个名为 privileges 的属性，用于存储一个由字符串组成的列表。
# 编写一个名为 show_privileges 的方法，它显示管理员的权限。
# 创建一个 Admin 的实例，并调用这个方法。
class Admin(User):
    """管理员信息"""
    def __init__(self, first_name, last_name, age, height, marriage):
        """
        初始化父类属性
        添加 privileges 属性
        """
        super().__init__(first_name, last_name, age, height, marriage)
        self.privileges = []  #用于存储一个由字符串组成的列表
        
    def show_privileges(self):
        """显示管理员权限"""
        if self.privileges:
            for privileges in self.privileges:
                print("- " + privileges.title())
        else:
            print("\nSorry, you are not privileges.")
            
zhu = Admin('yulong', 'zhu', 31, 181, 'no')
zhu.describe_user()

print("Privileges:")
zhu_privileges = ['can add post', 'can delete post', 'can ban user']

zhu.privileges = zhu_privileges
zhu.show_privileges()
