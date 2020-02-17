# coding: GBK 
"""һ������Ա��Ϣ������"""
from user import User
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
