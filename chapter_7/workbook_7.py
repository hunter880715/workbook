# coding: GBK 
# 7-1 �������ޣ���дһ�����򣬷����û�Ҫ����ʲô��������������ӡһ����Ϣ��
# ��"Let me see if I can find you a Subalu."
car = "What kind of car woule you like to rent? "
car += "\nPlease tell me the name of the car: "
name = input(car)
print("Let me see if I can find you a " + name + ".\n")
# 7-2 �͹ݶ�λ����дһ������ѯ���û��ж������ò͡�
# ������� 8 �ˣ��ʹ�ӡһ����Ϣ��ָ��û�п���������ָ���п�����
seats = input("��������λ��\n ")
seats = int(seats)
if seats >= 8:
    print("�Բ������ǵ�λ�ò����ˡ�\n")
else:
    print("���Եȣ�����Ϊ������λ�á�\n")
# 7-3 10 �ı��������û�����һ�����֣���ָ����������Ƿ��� 10 ����������
number = input("������һ�����֣��������������Ƿ��� 10 ���������� ")
number = int(number)
if number % 10 == 0:
    print("True.\n")
else:
    print("False.\n")
# 7-4 �������ϣ���дһ��ѭ������ʾ�û�����һϵ�е��������ϣ������û�����"quit"ʱ����ѭ����
# ÿ���û�����һ�����Ϻ󣬶���ӡһ����Ϣ��˵���ǻ�������������������ϡ�
# 7-6 �������ڣ�ʹ�ñ��� active ����ѭ��������ʱ����
# ʹ�� break ������û�����'quit'ʱ�˳�ѭ����
# ʹ�ñ��� active ����ѭ���ĸ�ʽ
pizza = "\nWhat kind og toppings would you like to add?(���� 1)"
pizza += "\nPlease enter here (enter 'quit' exit): "
active = True
while active:
    message = input(pizza)
    if message == 'quit':
        active = False
    else:
        print("\nThe addition was successful for you.\n")
# ʹ�� continue ������ѭ����ʽ��       
pizza = "\nWhat kind of toppings would you like to add?(���� 2)"
pizza += "\nPlease enter here (enter 'quit' exit): "
active = True
while active:
    message = input(pizza)
    if message == 'quit':
        active = False
    else:
        continue
        print("\nThe addition was successful for you.\n")
# ʹ�� break ������ѭ����ʽ��
pizza = "\nWhat kind of toppings would you like to add?(���� 3)"
pizza += "\nPlease enter here (enter 'quit' exit)�� "
while True:                  
    message = input(pizza)
    if message == 'quit':
        break
    else:
        print("\nThe addition was successful for you.\n")
# 7-5 ��ӰƱ���мҵ�ӰԺ���ݹ��ڵ�������ȡ��ͬ��Ʊ�ۣ�
# ��������Ĺ�����ѣ�3~12 ��Ĺ���Ϊ 10 ��Ԫ������ 12 ���Ϊ 15 ��Ԫ��
# ���дһ��ѭ����������ѯ���û������䣬��ָ����Ʊ�ۡ�
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
# 7-7 ����ѭ������дһ��û��û�˵�ѭ����������������Ctrl + C ��ֹ���У�
x = 0
while x < 5:
    x += 1
    print(x)
# 7-8 ��ʳ�꣺����һ����Ϊ sandwich_orders ���б������а������������ε����֡�
# �ڴ���һ����Ϊ finished_sandwiches �Ŀ��б�
# �����б� sandwich_orders �������е�ÿ�������Σ�����ӡһ����Ϣ���������Ƶ����б��С�
# �����ζ������ú󣬴�ӡһ����Ϣ������Щ�������г�����
sandwich_orders = ['cheese sandwich', 'french sandwich', 'pastrami sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI made your tuna sandwich " + sandwich.title())
    finished_sandwiches.append(sandwich)
print("\nSandwich:")
for finished_sandwiches in finished_sandwiches:
    print('\n' + finished_sandwiches.title())  
# 7-9 ����Ѭţ�������ˣ�����һ���б���ȷ��'pastrami'�����г����������Ρ�
# �ڳ���ͷ���һ�д��룺��ӡһ����Ϣ��ָ����ʳ�������Ѭţ�������ˡ�
# ʹ�� while ѭ�����б���'pastrami'ȫ��ɾ��������ȷ���б��ڲ��ٰ���'pastrami'��
menus = ['cheese', 'pastrami', 'tomato', 'pastrami', 'pastrami']
print("\nSorry,'pastrami' is have noting laft.")
while 'pastrami' in menus:
    menus.remove('pastrami')
print(menus)
# 7-10 ����Ķȼ�ʤ�أ���дһ�����򣬵����û�����Ķȼ�ʤ�أ���дһ����ӡ����Ĵ���顣
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
