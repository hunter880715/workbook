# coding: GBK 
# 9-5 尝试登陆次数：在为完成练习 9-3 编写的 User 类中，添加一个名为 login_attempts 的属性。
# 编写一个名为 increment_login_attempts() 的方法，它将属性 login_attempts 的值加 1。
# 再编写一个名为 reset_login_attempts() 的方法，它将属性 login_attempts 的值重置为 0 。
class User():
    """个人信息"""
    def __init__(self, first_name, last_name, age, height, marriage):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.marriage = marriage
        # 添加 login_attempts 属性
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
