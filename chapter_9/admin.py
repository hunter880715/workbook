# coding: GBK 
"""一个管理员信息属性类"""
from user import User
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
