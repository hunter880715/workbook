# 5-1 条件测试：编写一系列条件测试；
# 将每个测试以及对结果的预测和实际结果都打印出来。
# 编写的代码应类似于下面这样：
car = "subaru" # 示例
print("Is car == 'subaru'?I predict True.")
print(car == "subaru") # 结果正确
print("\nIs car == 'audi'?I predict False.")
print(car == "audi") # 结果错误
# 创建至少5个测试，且其中结果为 True 和 False 的测试都至少有5个。
# 1：
food = 'pizza'
print("\nIs food == 'pizza'?I'm True.")
print(food == 'pizza')
print("\nIs food == 'hanberge'?I'm False.")
print(food == 'hanberge')
# 2:
car = 'honda'
print("\nI think this's a honda.")
print(car == 'honda')
print("\nI think this's a suzuki.")
print(car == 'suzuki')
# 3:
player = 'lukazi'
print("\n下面出场的是'lukazi'!")
print(player == 'lukazi')
print("\n下面出场的是'luoning'!")
print(player == 'luoning')
# 4:
eat = '米饭'
print("\n今晚吃米饭？")
print(eat == '米饭')
print("\n今晚吃馒头？")
print(eat == '馒头')
# 5：
name = '李安'
print("\nYou name is '李安'？")
print(name == '李安')
print("\nYou name is '长盛'？")
print(name == '长盛')
# 5-2更多的条件测试：对下面列出的各种测试，至少编写一个结果为 True 和 False的。
# 检查两个字符串相等和不等。
my_car = 'toyota'
print(my_car == 'toyota')
print(my_car != 'toyota')
# 使用函数 lower() 的测试。
my_food = 'Pizza'
print(my_food == 'pizza')
print(my_food.lower() == 'pizza')
# 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
number = 20
number_1 = 30
print(number == number_1)
print(number != number_1)
print(number < number_1)
print(number > number_1)
print(number <= number_1)
print(number >= number_1)
# 使用关键字 and 和 or 测试。
print(number < 30 and number_1 == 30)
print(number < 30 and number_1 >= 27)
print(number <= 30 or number_1 < 30)
print(number == 13 or number_1 > 10)
# 测试特定的值是否包含在列表中。
motorcycles = ['toyota','honda','yamaha']
moto = 'honda'
if moto in motorcycles:
    print("Yes.")
# 测试特定的值是否未包含在列表中。
moto = 'Lifan'
if moto not in motorcycles:
    print("No.")
