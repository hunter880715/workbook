# coding: GBK 
# 9-11 创建一个 Admin 实例并对其调用方法 show_privileges()，以确认一切都能正确的运行。
from user import User

my_admin = User('yulong', 'zhu', 31, 181, 'no')
my_admin.describe_user()
