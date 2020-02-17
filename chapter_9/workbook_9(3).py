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

class Admin(User):
    """管理员信息"""
    def __init__(self, first_name, last_name, age, height, marriage):
        """
        初始化父类属性
        添加 privileges 属性
        """
        super().__init__(first_name, last_name, age, height, marriage)
        self.privileges = Privileges()  # 实例用作属性
        
    def show_privileges(self):
        """显示管理员权限"""
        print("Administration authority:")
        for privileges in self.privileges:
            print("- " + privileges.title())
# 9-8 权限：编写一个名为 privileges 的类，它只有一个属性——privileges，其中存储了 9-7 的列表。
# 讲方法 show_privileges() 移到这个类中。
# 在 Admin 类中，将一个 Privileges 实例用作其属性。
# 创建一个 Admin 实例，并使用方法 show_privileges() 来显示其权限。
class Privileges():
    """管理权信息"""
    def __init__(self, privileges=[]):
        """初始化属性"""
        self.privileges = privileges
        
    def show_privileges(self):
        """显示管理员权限"""
        print("Administration authority:")
        if self.privileges:
            for privileges in self.privileges:
                print("- " + privileges.title())
        else:
            print("- This user has no privileges.")
    
zhu = Admin('yulong', 'zhu', 31, 181, 'no')
zhu.describe_user()

zhu.privileges.show_privileges()

print("\nAdding privileges...")
zhu_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]
zhu.privileges.privileges = zhu_privileges
zhu.privileges.show_privileges()
