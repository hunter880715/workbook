# coding: GBK 
# 11-3 雇员：编写一个名为 Employee 的类，其方法__init__()接受名，姓和年薪，并将它们都存储在属性中。
# 编写一个名为 give_raise() 的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加。
class Employee():
    """雇员的信息"""
    
    def __init__(self, first, last, salary):
        """初始化属性"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """默认增加薪水5000"""
        self.salary += amount
