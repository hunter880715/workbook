# coding: GBK 
# 9-12 创建一个文件，在其中创建一个 Admin 的实例；
# 对其调用方法 show_privileges，以确认一切都依然能够正确的运行。
from user import User
from admin import Admin, Privileges

zhu = Admin('yulong', 'zhu', 31, 181, 'no')
zhu.describe_user()

zhu_1 = ['can add port', 'can delete port', 'can ban user']
zhu.privileges.privileges = zhu_1
zhu.privileges.show_privileges()
