# coding: GBK 
class User():
    """������Ϣ"""
    def __init__(self, first_name, last_name, age, height, marriage):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.marriage = marriage
        self.login_attempts = 0
    
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
        
    def increment_login_attempts(self):
        """������ login_attempts ��ֵ�� 1 """
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """������ login_attempts ��ֵ����"""
        self.login_attempts = 0

class Admin(User):
    """����Ա��Ϣ"""
    def __init__(self, first_name, last_name, age, height, marriage):
        """
        ��ʼ����������
        ��� privileges ����
        """
        super().__init__(first_name, last_name, age, height, marriage)
        self.privileges = Privileges()  # ʵ����������
        
    def show_privileges(self):
        """��ʾ����ԱȨ��"""
        print("Administration authority:")
        for privileges in self.privileges:
            print("- " + privileges.title())
# 9-8 Ȩ�ޣ���дһ����Ϊ privileges ���࣬��ֻ��һ�����ԡ���privileges�����д洢�� 9-7 ���б�
# ������ show_privileges() �Ƶ�������С�
# �� Admin ���У���һ�� Privileges ʵ�����������ԡ�
# ����һ�� Admin ʵ������ʹ�÷��� show_privileges() ����ʾ��Ȩ�ޡ�
class Privileges():
    """����Ȩ��Ϣ"""
    def __init__(self, privileges=[]):
        """��ʼ������"""
        self.privileges = privileges
        
    def show_privileges(self):
        """��ʾ����ԱȨ��"""
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
