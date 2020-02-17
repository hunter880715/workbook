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

# 9-7 ����Ա��һ��������û�����дһ����Ϊ Admin ���࣬�����̳� 9-5 ��ϰ��д�� User �ࡣ
# ���һ����Ϊ privileges �����ԣ����ڴ洢һ�����ַ�����ɵ��б�
# ��дһ����Ϊ show_privileges �ķ���������ʾ����Ա��Ȩ�ޡ�
# ����һ�� Admin ��ʵ�������������������
class Admin(User):
    """����Ա��Ϣ"""
    def __init__(self, first_name, last_name, age, height, marriage):
        """
        ��ʼ����������
        ��� privileges ����
        """
        super().__init__(first_name, last_name, age, height, marriage)
        self.privileges = []  #���ڴ洢һ�����ַ�����ɵ��б�
        
    def show_privileges(self):
        """��ʾ����ԱȨ��"""
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
