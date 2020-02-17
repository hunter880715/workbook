# coding: GBK
# 9-14 骰子：模块 random 包含以各种方式生成随机数的函数；
# 其中 randint() 返回一个位于指定范围内的整数；
# 创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。
# 编写一个名为 roll_die 的方法，他打印位于 1 和骰子面数之间的随机数。
# 创建一个六面的骰子，再掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次。
from random import randint
class Die():
    """骰子信息"""
    def __init__(self, sides=6):
        """
        初始化骰子
        骰子面数默认值为 6
        """
        self.sides = sides
        
    def roll_die(self):
        """返回一个位于 1 和骰子面数之间的随机数"""
        return randint(1, self.sides)
        
    
d6 = Die()
d6_list = []
for roll in range(10):
    roll = d6.roll_die()
    d6_list.append(roll)
print(d6_list)

d10 = Die(sides=10)
d10_list = []
for roll in range(10):
    roll = d10.roll_die()
    d10_list.append(roll)
print(d10_list)

d20 = Die(sides=20)
d20_list = []
for roll in range(10):
    roll = d20.roll_die()
    d20_list.append(roll)
print(d20_list)


