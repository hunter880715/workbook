# coding: GBK
# 8-16:导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
# 在主程序文件中，使用各种方法导入这个函数，再调用它。
def persomal_profile(first_name, last_name):
    """个人信息"""
    full_name = first_name + " " + last_name
    name = full_name.title()
    print("My name is " + name + ".\n")
