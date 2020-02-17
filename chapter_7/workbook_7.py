# coding: GBK 
# 7-1 汽车租赁：编写一个程序，访问用户要租赁什么样的汽车，并打印一条消息。
# 如"Let me see if I can find you a Subalu."
car = "What kind of car woule you like to rent? "
car += "\nPlease tell me the name of the car: "
name = input(car)
print("Let me see if I can find you a " + name + ".\n")
# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。
# 如果超过 8 人，就打印一条消息，指出没有空桌；否则指出有空桌。
seats = input("请问您几位？\n ")
seats = int(seats)
if seats >= 8:
    print("对不起，我们的位置不够了。\n")
else:
    print("请稍等，正在为您安排位置。\n")
# 7-3 10 的倍数：让用户输入一个数字，并指出这个数字是否是 10 的整倍数。
number = input("请输入一个数字，我来告诉你它是否是 10 的整倍数： ")
number = int(number)
if number % 10 == 0:
    print("True.\n")
else:
    print("False.\n")
# 7-4 披萨配料：编写一个循环，提示用户输入一系列的披萨配料，并在用户输入"quit"时结束循环。
# 每当用户输入一种配料后，都打印一条消息，说我们会在披萨中添加这种配料。
# 7-6 三个出口：使用变量 active 控制循环结束的时机。
# 使用 break 语句在用户输入'quit'时退出循环。
# 使用变量 active 结束循环的格式
pizza = "\nWhat kind og toppings would you like to add?(测试 1)"
pizza += "\nPlease enter here (enter 'quit' exit): "
active = True
while active:
    message = input(pizza)
    if message == 'quit':
        active = False
    else:
        print("\nThe addition was successful for you.\n")
# 使用 continue 语句结束循环格式。       
pizza = "\nWhat kind of toppings would you like to add?(测试 2)"
pizza += "\nPlease enter here (enter 'quit' exit): "
active = True
while active:
    message = input(pizza)
    if message == 'quit':
        active = False
    else:
        continue
        print("\nThe addition was successful for you.\n")
# 使用 break 语句结束循环格式。
pizza = "\nWhat kind of toppings would you like to add?(测试 3)"
pizza += "\nPlease enter here (enter 'quit' exit)： "
while True:                  
    message = input(pizza)
    if message == 'quit':
        break
    else:
        print("\nThe addition was successful for you.\n")
# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价：
# 不到三岁的观众免费；3~12 岁的观众为 10 美元；超过 12 岁的为 15 美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。
ticket = "\nPlease enter your age: "
while True:
    age = input(ticket)
    if age == 'quit':
        break
    elif int(age) <= 3:
        print("\nFree access.")
    elif 3 <int(age) <= 12:
        print("\n10 dollars,please.")
    else:
        print("\n15 dollars,please.")
# 7-7 无限循环：编写一个没完没了的循环，并运行它。（Ctrl + C 终止运行）
x = 0
while x < 5:
    x += 1
    print(x)
# 7-8 熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字。
# 在创建一个名为 finished_sandwiches 的空列表。
# 遍历列表 sandwich_orders 对于其中的每种三明治，都打印一条信息，并将其移到空列表中。
# 三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['cheese sandwich', 'french sandwich', 'pastrami sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI made your tuna sandwich " + sandwich.title())
    finished_sandwiches.append(sandwich)
print("\nSandwich:")
for finished_sandwiches in finished_sandwiches:
    print('\n' + finished_sandwiches.title())  
# 7-9 五香熏牛肉卖完了：创建一个列表，并确保'pastrami'在其中出现至少三次。
# 在程序开头添加一行代码：打印一条消息，指出熟食店的五香熏牛肉卖完了。
# 使用 while 循环将列表中'pastrami'全部删除，最终确认列表内不再包含'pastrami'。
menus = ['cheese', 'pastrami', 'tomato', 'pastrami', 'pastrami']
print("\nSorry,'pastrami' is have noting laft.")
while 'pastrami' in menus:
    menus.remove('pastrami')
print(menus)
# 7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地，编写一个打印结果的代码块。
tourism = {}
active = True
while active:
    name = input("\nWhat's your name?\n")
    city = input("\nIf you could visit one place in the world," + 
        "where would you go?\n")
    tourism[name] = city
    message = input("\nEnter exit(yes/no): \n")
    if message == 'yes':
        active = False
print("\n--- Poll Results ---")
for name, city in tourism.items():
    print("\n" + name.title() + " would like to " + city.title())
