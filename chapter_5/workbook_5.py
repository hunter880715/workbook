# coding: GBK 
# 5-3 ��������ɫ #1����������Ϸ����ɱ��һ�������ˣ�
# �봴��һ����Ϊ alien_color �ı�������������Ϊ'green','yellow'��'red'��
# ��дһ�� if ��䣬����������Ƿ�����ɫ�ģ�����ǣ��ʹ�ӡһ����Ϣ��ָ����һ���� 5 �㡣
aline_coler = 'green'
if aline_coler == 'green':
    print("To gain '5'.\n")
# �������ͨ���ˣ��ٴα�д��һ��δͨ���汾��
if aline_coler != 'green':
    print("To gain '5'.\n")
# 5-4 ��������ɫ #2���� 5-3 �������������˵���ɫ������дһ�� if-else �ṹ��
# �������������ɫ�ģ���ӡ��Ϣ��ָ����һ���� 5 �㡣
# ��������˲�����ɫ�ģ���ӡ��Ϣ��ָ����һ���� 10 �㡣
# ��д�������������汾��һ��ִ�� if ����飬һ��ִ�� else ����顣
aline_coler = 'green'
if aline_coler == 'green': # if �汾
    print("To gain '5'.")
else:
    print("To gain '10'.")

if aline_coler != 'green': # else �汾
    print("To gain '5'.")
else:
    print("To gain '10'.\n")
# 5-5 �����˵���ɫ #3������ϰ 5-4 �� if-else �ṹ��Ϊ if-elif-else �ṹ��
# �������������ɫ�ģ���ӡһ����Ϣ��ָ����һ���� 5 �㡣
# ����������ǻ�ɫ�ģ���ӡһ����Ϣ��ָ����һ���� 10 �㡣
# ����������Ǻ���ģ���ӡһ����Ϣ��ָ����һ���� 15 �㡣
# ��д�������������汾���ֱ���������Ϊ��ɫ����ɫ����ɫ�Ǵ�ӡһ����Ϣ��
aline_coler = 'green'       # ����������ɫ
if aline_coler == 'green':
    print("To gain '5'.")
elif aline_coler == 'yellow':
    print("To gain '10'.")
else:
    print("To gain '15'.")
aline_coler = 'yellow' # �������ǻ�ɫ
if aline_coler == 'green':
    print("To gain '5'.")
elif aline_coler == 'yellow':
    print("To gain '10'.")
else:
    print("To gain '15'.")
aline_coler = 'red' # �������Ǻ�ɫ
if aline_coler == 'green':
    print("To gain '5'.")
elif aline_coler == 'yellow':
    print("To gain '10'.")
else:
    print("To gain '15'.")
# 5-6 �����Ĳ�ͬ�׶Σ����ñ��� age ��ֵ����дһ�� if-elif-else �ṹ��
# ���� age ��ֵ�жϴ����������ĸ��׶Ρ�
age = 32
if age < 2:
    print("\nHe's a baby.") # Ӥ��
elif 2 < age < 4:
    print("\nHe's learning to walk.") # ����ѧ��
elif 4 < age < 13:
    print("\nHe's a child.") # ��ͯ
elif 13< age < 20:
    print("\nHe's a young man.") # ������
elif 20< age < 65:
    print("\nHe's an adult.") # ������
else:
    print("\nHe's an old man.") # ������
# 5-7 ϲ����ˮ��������һ���б����а���ϲ����ˮ����
# ��дһϵ�ж����� if ��䣬����б����Ƿ�����ض���ˮ����
# ���б�����Ϊ favorite_fruits���������а�������ˮ����
# ��д 5 �� if ��䣬ÿ�������ĳ��ˮ���Ƿ�������б��У�
# ����������б��У��ʹ�ӡһ����Ϣ����"You really like bananas!"
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
# 5-8 �����ⷽʽ������Ա���к�������һ�����ٰ��� 5 λ�û������б�����һ����Ϊ'admin'.
# ������Ҫ��д�Ĵ��룬��ÿλ�û���¼��վ�󶼴�ӡһ���ʺ���Ϣ��
# �����û����б�����ÿһλ�û���ӡһ���ʺ���Ϣ��
# ����û���Ϊ"admin",�ʹ�ӡһ�������ʺ���Ϣ�������ӡһ����ͨ���ʺ���Ϣ��
# 5-9 ����û���û������Σ�
# ��Ϊ�����ϰ 5-8 ��д�ĳ����У����һ�� if ��䣬����б��Ƿ�Ϊ�ա�
# ���Ϊ�գ��ʹ�ӡ��Ϣ"We need to find some users!"
# ɾ���б��е������û�����ȷ����ӡ��ȷ����Ϣ��
users = ['moka','louse','admin','lilei','anni']
if users: # �б�Ϊ�յ������
    for user in users: # ���ⷽʽ������Ա���к���
        if user == 'admin':
            print("\nHello" + user.title() + 
            ",would you like to see a status report?")
        else: # ��ͨ��ʽ���û��Ǵ��к���
            print("\nHello" + user.title() + 
            ",think you for logging in again.")
else: # �б�Ϊ�յĴ�ӡ��
    print("\nWe need to find some users!")
# 5-10 ����û�������дһ������ģ����վȷ��ÿλ�û����û�������һ�޶��ķ�ʽ��
# ����һ�����ٰ��� 5 ���û������б�������Ϊ current_users.
# ����һ���µİ��� 5 ���û������б�������Ϊ new_users��
# ȷ��������һ�����û���Ҳ�������б� current_users �С�
# �����б� new_users���������е�ÿ���û�������������Ƿ��ѱ�ʹ�á�
# �����ʹ�þʹ�ӡһ����Ϣ��ָ����Ҫ�������û�����
# ���򣬴�ӡһ����Ϣ��ָ������û���δ��ʹ�á�
# ȷ���Ƚ�ʱ�����ִ�Сд��
current_users = ['moka','louse','admin','lilei','anni']
new_users = ['lilei','hanmei','admin','fathon','suman']
current_user_lower = [current_user.lower() 
        for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in current_user_lower: # Ϊ�����ִ�Сд���ڴ�Ӧ�� lower()��
        print("\n" + new_user + " " + "cant use,plese try again.")
    else:
        print("\n" + new_user + ",welcome to use it.")
# 5-11 ������������ʾλ�ã��� 1st �� 2nd������������� th ��β��ֻ�� 1��2��3 ���⡣
# ��һ���б��д洢���� 1~9.
# ��������б�
# ��ѭ����ʹ��һ�� if-elif-else �ṹ���Դ�ӡÿ�����ֶ�Ӧ��������
# �������ӦΪ 1st��2nd��3rd��4th��5th���� ��ÿ��������ռһ�С�
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
