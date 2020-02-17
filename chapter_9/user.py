# coding: GBK 
# 9-11 ���� Admin �ࣺ����ϰ 9-8 Ϊ�������� User��Privileges �� Admin ��洢��һ��ģ���С�
"""һ�������û����Ե���"""
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
