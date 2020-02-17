# coding: GBK 
# 9-5 ���Ե�½��������Ϊ�����ϰ 9-3 ��д�� User ���У����һ����Ϊ login_attempts �����ԡ�
# ��дһ����Ϊ increment_login_attempts() �ķ������������� login_attempts ��ֵ�� 1��
# �ٱ�дһ����Ϊ reset_login_attempts() �ķ������������� login_attempts ��ֵ����Ϊ 0 ��
class User():
    """������Ϣ"""
    def __init__(self, first_name, last_name, age, height, marriage):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.marriage = marriage
        # ��� login_attempts ����
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

zhu = User('yulong', 'zhu', 31, 181, 'no')
zhu.describe_user()
zhu.greet_user()

print("Making 5 login attempts......")
zhu.increment_login_attempts()
zhu.increment_login_attempts()
zhu.increment_login_attempts()
zhu.increment_login_attempts()
zhu.increment_login_attempts()
print("Resetting login attempts: " + str(zhu.login_attempts) + "\n")

zhu.reset_login_attempts()
print("Login attempts: " + str(zhu.login_attempts) + "\n")
