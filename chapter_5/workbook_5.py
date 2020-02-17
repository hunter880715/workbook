# coding: GBK 
# 5-3 外星人颜色 #1：假设在游戏中射杀了一个外星人；
# 请创建一个名为 alien_color 的变量，将其设置为'green','yellow'或'red'。
# 编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了 5 点。
aline_coler = 'green'
if aline_coler == 'green':
    print("To gain '5'.\n")
# 上面测试通过了，再次编写另一个未通过版本。
if aline_coler != 'green':
    print("To gain '5'.\n")
# 5-4 外星人颜色 #2：像 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
# 如果外星人是绿色的，打印消息，指出玩家获得了 5 点。
# 如果万星人不是绿色的，打印消息，指出玩家获得了 10 点。
# 编写这个程序的两个版本，一个执行 if 代码块，一个执行 else 代码块。
aline_coler = 'green'
if aline_coler == 'green': # if 版本
    print("To gain '5'.")
else:
    print("To gain '10'.")

if aline_coler != 'green': # else 版本
    print("To gain '5'.")
else:
    print("To gain '10'.\n")
# 5-5 外星人的颜色 #3：将练习 5-4 的 if-else 结构改为 if-elif-else 结构。
# 如果外星人是绿色的，打印一条消息，指出玩家获得了 5 点。
# 如果外星人是黄色的，打印一条消息，指出玩家获得了 10 点。
# 如果外星人是红儿的，打印一条消息，指出玩家获得了 15 点。
# 编写这个程序的三个版本，分别在外星人为绿色、黄色、红色是打印一条消息。
aline_coler = 'green'       # 外星人是绿色
if aline_coler == 'green':
    print("To gain '5'.")
elif aline_coler == 'yellow':
    print("To gain '10'.")
else:
    print("To gain '15'.")
aline_coler = 'yellow' # 外星人是黄色
if aline_coler == 'green':
    print("To gain '5'.")
elif aline_coler == 'yellow':
    print("To gain '10'.")
else:
    print("To gain '15'.")
aline_coler = 'red' # 外星人是红色
if aline_coler == 'green':
    print("To gain '5'.")
elif aline_coler == 'yellow':
    print("To gain '10'.")
else:
    print("To gain '15'.")
# 5-6 人生的不同阶段：设置变量 age 的值，编写一个 if-elif-else 结构；
# 根据 age 的值判断处于人生的哪个阶段。
age = 32
if age < 2:
    print("\nHe's a baby.") # 婴儿
elif 2 < age < 4:
    print("\nHe's learning to walk.") # 蹒跚学步
elif 4 < age < 13:
    print("\nHe's a child.") # 儿童
elif 13< age < 20:
    print("\nHe's a young man.") # 青少年
elif 20< age < 65:
    print("\nHe's an adult.") # 成年人
else:
    print("\nHe's an old man.") # 老年人
# 5-7 喜欢的水果：创建一个列表，其中包含喜欢的水果；
# 编写一系列独立的 if 语句，检查列表中是否包含特定的水果。
# 将列表命名为 favorite_fruits，并在其中包含三种水果。
# 编写 5 条 if 语句，每条都检查某种水果是否包含在列表中；
# 如果包含在列表中，就打印一条消息，如"You really like bananas!"
favorite_fruits = ['banana','apple','orange']
if 'banana' in favorite_fruits:
    print('\nI really like bananas!')
if 'apple' in favorite_fruits:
    print('\nI really like apple!')
if 'orange' in favorite_fruits:
    print('\nI really like orange!')
if 'grapes' in favorite_fruits:
    print('\nI really like grapes!')
if 'pomegranate' in favorite_fruits:
    print('\nI really like pomegranate!')
# 5-8 以特殊方式跟管理员打招呼：创建一个至少包含 5 位用户名的列表，其中一个名为'admin'.
# 想象你要编写的代码，在每位用户登录网站后都打印一条问候消息。
# 遍历用户名列表，并向每一位用户打印一条问候消息。
# 如果用户名为"admin",就打印一条特殊问候消息。否则打印一条普通的问候消息。
# 5-9 处理没有用户的情形：
# 在为完成练习 5-8 编写的程序中，添加一条 if 语句，检查列表是否为空。
# 如果为空，就打印消息"We need to find some users!"
# 删除列表中的所有用户名，确定打印正确的消息。
users = ['moka','louse','admin','lilei','anni']
if users: # 列表为空的情况。
    for user in users: # 特殊方式跟管理员打招呼。
        if user == 'admin':
            print("\nHello" + user.title() + 
            ",would you like to see a status report?")
        else: # 普通方式跟用户们打招呼。
            print("\nHello" + user.title() + 
            ",think you for logging in again.")
else: # 列表为空的打印。
    print("\nWe need to find some users!")
# 5-10 检查用户名：编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
# 创建一个至少包含 5 个用户名的列表，并命名为 current_users.
# 创建一个新的包含 5 个用户名的列表，并命名为 new_users；
# 确保其中有一两个用户名也包含在列表 current_users 中。
# 遍历列表 new_users，对于其中的每个用户名，都检查它是否已被使用。
# 如果被使用就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写。
current_users = ['moka','louse','admin','lilei','anni']
new_users = ['lilei','hanmei','admin','fathon','suman']
current_user_lower = [current_user.lower() 
        for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in current_user_lower: # 为不区分大小写，在此应用 lower()。
        print("\n" + new_user + " " + "cant use,plese try again.")
    else:
        print("\n" + new_user + ",welcome to use it.")
# 5-11 序数：序数表示位置，如 1st 和 2nd。大多数序数以 th 结尾，只有 1、2、3 例外。
# 在一个列表中存储数字 1~9.
# 遍历这个列表。
# 再循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。
# 输出内容应为 1st、2nd、3rd、4th、5th…… 但每个序数独占一行。
numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print("\n" + str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
