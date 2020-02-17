# coding: GBK 
# 6-1 使用一个字典啦存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应当包含键 first_name, last_name, age 和 city.
# 将存储在字典中的每项信息都打印出来。
personal_data = {
    'first_name':'hunter',
    'last_name':'zhu',
    'age':'31',
    'city':'yantai',
    }
for key, value in personal_data.items():     # 调取 items() 并循环的打印方法。
    print(key.title() +": " + value.title())
# 普通方式打印。    
print("First name: " + personal_data['first_name'].title())
print("Last name: " + personal_data['last_name'].title())
print("Age: " + personal_data['age'])
print("Habitable city: " + personal_data['city'].title() + "\n")
# 6-2 喜欢的数字：使用一个字典存储一些人喜欢的数字。
# 想出五个人的名字，并将这些名字用作字典中的键；
# 打印每个人的名字和喜欢的数字。
favorite_number = {
    'zhao': 19,
    'qian': 22,
    'sun': 12,
    'lee': 30,
    'wu': 7,
    }
for name, number in favorite_number.items():  # 调取 times() 并循环的打印方法。
    print(name.title() + 
    "'s favorite number is: " + str(number) + ".\n")
# 普通打印方法。
print("Zhao's favorite number is " + str(favorite_number['zhao']) + ".\n")
print("Qian's favorite number is " + str(favorite_number['qian']) + ".\n")
print("Sun's favorite number is " + str(favorite_number['sun']) + ".\n")
print("Lee's favorite number is " + str(favorite_number['lee']) + ".\n")
print("Wu's favorite number is " + str(favorite_number['wu']) + ".\n")
# 6-3 词汇表：Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为“词汇表”。
# 想出在前面学过的 5 个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义；
# 可以在一行打印词汇，在使用换行符插入一个空行，让后在下一行以缩进的方式打印词汇的含义。
glossaries = {
    'print': '打印信息',
    'for': '循环语句',
    'if': '分支语句',
    'else': '跳转',
    'del': '删除元素'
    }
print("print: \n" + "\t" + glossaries['print'])
print("for: \n" + "\t" + glossaries['for'])
print("if: \n" + "\t" + glossaries['if'])
print("else: \n" + "\t" + glossaries['else'])
print("del: \n" + "\t" + glossaries['del'] + "\n")
# 6-4 词汇表 2：将 6-3 为练习编写的代码，将其中一系列语句替换为一个遍历字典中的键和值的循环；
# 确认循环无误后，再在词汇表中添加 5 个 Python 术语，并输出。
glossaries = {
    'print': '打印信息',
    'for': '循环语句',
    'if': '分支语句',
    'slse': '跳转',
    'del': '删除元素',
    'py': 'Python',
    'set()': '集合',
    'items()': '返回一个键-值对列表',
    'keys()': '只读取键',
    'values()': '只读取值'
    }
for key, value in glossaries.items():
    print('key: ' + key + '\n')
    print('value: ' + value + '\n')
# 6-5 河流：创建一个字典，在其中存储三条大河流及其2流经的国家。
# 使用循环为每条河流打印一条消息，如"The Nile runs through Egypt."。
rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'amazon': 'brazil',
    }
for key, value in rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title() + '.\n')
for river in rivers.keys():    # 使用循环将该字典中每条河流的名字都打印出来。
    print(river.title() + '\n')
for river in rivers.values():  # 使用循环将该字典中包含的每个国家名字都打印出来。
    print(river.title() + '\n')
# 6-6 调查：在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作：
# 创建一个应该会接受调查的人员名单，其中有些人已经包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人打印一条信息感谢，对未参与调查的人打印消息邀请调查。
favorite_languagse = {
    'jen': 'pthong',
    'sarah': 'c',
    'edward': 'ruby',
    }
friends = ['jam','jen','sarah','saru','edward']
for name in friends:
    if name in favorite_languagse.keys():
        print(name.title() + ",think you!\n")
    else:
        print(name.title() + ",please take our poll.\n")
# 6-7 人：在为完成练习 6-1 而编写的程序中，在创建两个表示人的字典；
# 将这三个字典都存储在一个名为 people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。
fmily_0 = {
    'first_name': 'yulong',
    'last_name': 'zhu',
    'age': 31,
    'city': 'longkou',
    }
fmily_1 = {
    'first_name': 'yan',
    'last_name': 'xu',
    'age': 62,
    'city': 'longkou',
    }
fmily_2 = {
    'first_name': 'xue',
    'last_name': 'zhu',
    'age': 38,
    'city': 'laiyang',
    }
people = [fmily_0, fmily_1, fmily_2]
for people in people:
    print(people)
    print('first name: ' + people['first_name'].title())
    print('last name: ' + people['last_name'].title())
    print('age: ' + str(people['age']))
    print('city: ' + people['city'].title() + '\n')
    
# 6-8 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
# 在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为 pets 的列表中，在遍历该列表，并将宠物的所有信息都打印出来。
wang = {
    'species': 'dog',
    'owner': 'tom',
    }
miao = {
    'species': 'cat',
    'owner': 'jack',
    }
qiou = {
    'species': 'bird',
    'owner': 'devid',
    }
pets = [wang, miao, qiou]
for pet in pets:
    print('\n' + 'spevies: ' + pet['species'].title())
    print('owner: ' + pet['owner'].title())
# 6-9 喜欢的地方：创建一个名为 favorite_places 的字典，在这个字典中，将三个人的名字作为键；
# 对于其中的每个人，都存储他喜欢的 1~3 个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {
    'wang': ['xinjiang', 'shanghai'],
    'zhang': ['shanghai','xian'],
    'lee': ['beijing', 'qingdao', 'weihai'],
    }

for name, place in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in place:
        print("\t" + place.title())
# 6-10 喜欢的数字：修改为完成 6-2 而编写的程序，让每个人都可以有多个喜欢的数字；
# 将每个人的名字及其喜欢的数字打印出来。
favorite_number = {
    'zhao': [3, 19],
    'qian': [12, 24, 44],
    'sun': [1, 8, 45],
    'lee': [4, 30],
    'wu': [7, 27],
    }
for name, numbers in favorite_number.items():
    print("\n" + name.title() + "'s favorote numbers are: ")
    for number in numbers:
        print("\t" + str(number))
# 6-11 城市：创建一个名为 cities 的字典，其中将三个城市名用作键；
# 对于每座城市都创建一个字典，并在其中包含该城市所属的 国家、人口约数以及一个有关的事实。
# 在表示每座城市的字典中，应包含 country、population 和 fact 等键。
# 将每座城市的名字以及有关它们的信息都打印出来。
cities = {
    'new york': {
        'country': 'america',
        'population': 8510000,
        'fact': 'economic center',
        },
    'shanghai': {
        'country': 'china',
        'population': 24240000,
        'fact': 'flourshing',
        },
    'aleppo': {
        'country': 'syria',
        'population': 2300000,
        'fact': 'civil war',
        },
    }
for cityname, city_info in cities.items():
    print('\n' + 'cityname: ' + cityname.title())
    # 书中例题格式：
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print('\t' + "country: " + country.title())
    print('\t' + "population: " + str(population))
    print('\t' + "fact: " + fact)
    # 改进输出格式：
    for key, value in city_info.items():
        print('\t' + key.title() + ': ' + str(value))
