#! python3
# 4-1 披萨：相处至少三种披萨，将其名字存储在一个列表中，再使用 for 循环打印出来。
# 修改这个 for 循环，使其打印包含披萨名称的句子，而不仅仅是披萨的名字。
# 对于每种披萨，都显示一行输出。
# 在程序末尾添加一行代码，它不在 for 循环当中，指出有多喜欢披萨。
# 输出应包含针对每种披萨的消息，还有一个总结性的句子。
pizzas = ["pizzahut","domino's pizza","champion pizza"]
for pizza in pizzas:
    print(pizza)
    print("I like" + " " + pizza.title() + "!")
    print(pizza.title() + "!" + "My baby,my life,my love!\n")
print("I really love pizza!\n")
# 4-2 动物：想出至少三种有共同特征的动物；
# 将它们的名字储存在一个列表中， for 循环打印。
# 修改这个程序，使其针对每种动物都打印出来一个句子。
# 在程序末尾添加一行代码，指出这些动物的共同之处。
animals = ["dag","cat","rabbit"]
for animal in animals:
    print(animal)
    print("A" + " " + animal + " " + "would make a great pet.\n")
print("Any of these animals would make a great pet!\n")
# 4-3 数到 20：使用一个 for 循环打印数字 1~20.
for value in range(1,21):
    print(value)
# 4-4 (见附件：workbook_3(1).py）
# 4-5 计算 1~1000000 的总和：创建一个列表，其中包含数字 1~1000000；
# 使用 min() 与 max() 核实该列表确实是从 1 开始，到 1000000 结束；
# 对这个列表调用函数 sum()，看看Python将一百万个数字相加需要多长时间。
digits = list(range(1,1000001))
print(min(digits))
print(max(digits))
print(sum(digits))
# 4-6 奇数：通过给函数 range() 指定第三个参数来创建一个列表，其中包含 1~20 的奇数；
# 再使用一个 for 循环将这些数字都打印出来。
numbers = list(range(1,21,2))
print(numbers)
for number in numbers:
    print(number)
# 4-7 3的倍数：创建一个列表，其中包含3~30内能被3整除的数字；
# 使用for循环将这个列表中的数字打印出来。
numbers = list(range(3,31,3))
print(numbers)
for number in numbers:
    print(number)
# 4-8 立方：创建一个列表，其中包含前10个整数（即1~10）的立方；
# 使用for循环将这些立方数打印出来。
squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares)
for value in squares:
    print(value)
# 4-9 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方。
square = [value**3 for value in range(1,11)]
print(square)
# 4-10 切片：选择在本章编写的一个程序，在末尾添加几行代码，完成下面的任务；
# 打印消息"The first three items in the list are:",再切片打印前三个元素。
# 打印消息"Three items from the middle of the list are:",打印中间三个元素。
# 打印消息"The last three items in the list are:",打印列表末尾的三个元素。
players = ["hai","tom","jack","woman","man"]
print("\nThe first three items in the list are:")
for player in players[:3]:
    print(player.title())
print("\nThree iteams from the middle of the list are:")
for player in players[1:4]:
    print(player.title())
print("\nThe last three items in the list are:")
for player in players[2:]:
    print(player.title())
# 4-11 你的披萨和我的披萨：在完成练习4-1编写的 程序中，创建披萨列表的副本；
# 将副本存储到变量 friend_pizzas 中，在完成下面的任务。
# 在原来的披萨列表中再添加一种披萨。
# 在列表 fried_pizzas 中添加另一种披萨。
# 核实两个不同的列表。打印消息"My favorite pizzas are:",for循环来打印第一个列表。
# 打印消息"My friend's favorite pizzas are:",使用for循环来打印第二个列表。
my_pizzas = ["pizzahut","domino's pizza","champion pizza"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("big pizza")
print(my_pizzas)
friend_pizzas.append("bigjion pizza")
print(friend_pizzas)
print("\nMy favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza.title())
print("\nMy friend's favotite pizza are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
# 4-12 使用多个循环：请选择树种一个版本的 food.py，在其中编写两个 for 循环打印出来。
# NO.1 例题 for 循环补全。
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("\nMy favorite foods are:")
for my_foods in my_foods:
    print(my_foods)
print("\nMy friend's favorite foods are:")
for friend_foods in friend_foods:
    print(friend_foods)
# NO.2例题for循环补全。
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
for my_foods in my_foods:
    print(my_foods)
print("\nMy friend's foods are:")
for friend_foods in friend_foods:
    print(friend_foods)
# 4-13 自助餐：有一家自助餐厅，只提供五种自助餐，想出五种食品存储在一个元组中。
# 使用一个 for 循环将餐厅提供的五种食品打印出来。
# 尝试修改其中的一个元素，核实Python确实会拒绝这样做。（已核实）
foods = ("土豆丝","酸菜鱼","炸里脊","糖醋排骨","杂菌汤")
for food in foods:
    print(food)
# 餐厅调整了菜单，替换了其中两道菜品，编写一个这样的代码块：
# 给元组变量赋值，并使用一个for循环将新元组的每个元素都打印出来。
foods = ("土豆烧牛肉","水煮鱼","炸里脊","糖醋排骨","杂菌汤")
for food in foods:
    print(food)
# 4-4 一百万：创建一个列表，包含数字 1~1000000，再使用 for 循环打印出来。
milions = list(range(1,1000001))
print(milions)
for milion in milions:
    print(milion)


# 八天的学习成果，从丝毫没有接触的小白一个，如今也开始入门，希望自己今后继续努力。
# 之后的计划是，最好一个星期~10 天内能够学习四个章节；
# 争取在 2019 年年底，2020 年到来之前着两个多月内，将这本《Python从入门到实践》学完。
# 之后还计划着学完入门后，能够磕磕碰碰看些资料的时候，再开始着手新语言的入门。
# 前四章的学习小结就这些吧。
# 2019.11.10
    
