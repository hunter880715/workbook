# coding: GBK 
# 8-1 消息：编写一个名为 display_message() 的函数；
# 打印一个句子，指出在这章学的是什么。调用这个函数，确认显示的信息正确无误。
def display_message():
    """本章所学内容"""
    print("编写函数与调用函数。\n")
display_message()
# 8-2 喜欢的图书：编写一个名为 favorite_book 的函数，其中包含一个名为 title 的形参。
# 这个函数打印一条消息，调用这个函数，并将以本土数的名称作为实参传递给他。
def favorite_book(title):
    """喜欢的书名"""
    print("One of my favorite books is " + title.title() + ".\n")
favorite_book("golden slumber")
# 8-3 T恤：编写一个名为 make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件T恤，再使用关键字实参来调用这个函数。
def make_shirt(siza, typeface):
    """T恤的尺码与字样"""
    print("The T-shirt siza is " + siza + ";\n" + 
    "typeface: " + typeface + ".\n")
make_shirt("XXL", "I love Python")               # 使用位置实参调用函数。
make_shirt(siza='XXL', typeface="I love Python") # 使用关键字实参调用函数。
# 8-4 大号T恤：修改函数 make_shirt()，使其在默认的情况下制作印有'I love Python'的大号T恤。
# 调用这个函数来制作如下T恤：
# 一件印有默认字样的大号T恤、一件印有默认字样的中号T恤以及印有其他字样的T恤。
def make_shirt(siza, typeface='I love Python'):
    """T恤的尺码与字样"""
    print("The T-shirt siza is " + siza + ";\n" +
    "typeface: " + typeface + ".\n")
make_shirt("XXXL")  # 大号T恤
make_shirt("L")     # 中号T恤
make_shirt(siza="M", typeface="I love China") # 其他字样T恤
# 8-5 城市：编写一个名为 describe_city() 的函数，它接受一个名字以及该城市所属的国家。
# 这个函数打印一个句子，如 Reykjavik is in Iceland.
# 给用于存储国家的形参指定默认值，魏三做不同的城市调用这个函数，且其中至少有一座城市不属于这个国家。
def describe_city(city, country="china"):
    """城市与所属国家"""
    print(city.title() + " is in " + country.title() + ".\n")
describe_city('chongqing')
describe_city('shanghai')
describe_city('landen', country='england')
# 8-6 城市名：编写一个名为 city_country() 的函数，它接受城市的名称及其所属国家。
# 这个函数应发挥一个格式类似于这样的字符串："Santiago,Chile"
# 至少使用三个城市-国家对调用这个函数，并打印它的返回值。
def city_country(city_name, country_name):
    """城市名及其所属国家"""
    full = city_name + "," + country_name
    return full.title()
mess = city_country("beijing", "china")
print(mess)
mess = city_country("tokiyo", "japan")
print(mess)
mess = city_country("new york", "america")
print(mess)
# 8-7 专辑：编写一个名为 make_album() 的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，核实字典正确的存储了专辑的信息。
def make_album(singer_name, album_name):
    """歌手名与专辑名"""
    album = {'singer':singer_name, 'album':album_name}
    return album
album_1 = make_album('alan walker', 'faded')
print(album_1)
album_2 = make_album('taylor swfit', '1989')
print(album_2)
album_3 = make_album('katy perry', 'teenage dteam')
print(album_3)
# 给函数 make_album() 添加一个可选形参，以便能够存储专辑所包含的歌曲数。
# 如果调用这个函数时制定了歌曲数，就将这个值添加到表示专辑的字典中。
# 调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(singer_name, album_name, number=''):
    """歌手、专辑的名字以及歌曲数量"""
    album = {'singer':singer_name, 'album':album_name}
    if number:
        album['number'] = number
    return album
album_1 = make_album('alan walker', 'faded', number=12)
print(album_1)
album_2 = make_album('taylor swfit', '1989')
print(album_2)
album_3 = make_album('katy perry', 'teenage dteam', number=14)
print(album_3)
# 8-8 用户的专辑：在 8-7 练习编写的程序中，编写一个 while 循环，让用户输入一个歌手和专辑名。
# 获取这些信息后，使用他们来调用函数 make_album()，并将创建的字典打印出来。
# 在这个 while 循环中，务必要提供退出途径。
def make_album(singer_name, album_name, number=''):
    """歌手、专辑的名字以及歌曲数量"""
    album = {'singer':singer_name, 'album':album_name}
    if number:
        album['number'] = number
    return album
while True:
    print("\nPlease tell me you like the singer and album;")
    print("(enter 'n' to quit)")
    singer = input("Do you like singer name: ")
    if singer == 'n':
        break
    album = input("DO you like album name is: ")
    if album == 'n':
        break
    number = input("How many songs are on the album: ")
    if number == 'n':
        break
    message = input("Exit(y/n):")
    if message == 'n':
        break
albums = make_album(singer, album, number)
print(albums)
# 8-9 魔术师：创建一个包含魔术师名字的列表，并将其传送给名为 show_magicians() 的函数。
# 这个函数打印列表中每个魔术师的名字。
def show_magicians(names):
    """魔术师的名字"""
    for name in names:
        print(name.title())
magicians = ['lee', 'jake', 'tom']
show_magicians(magicians)
# 8-10 了不起的魔术师：在为完成练习 8-9 所编写的程序中，编写一个名为 make_great() 的函数；
# 对魔术师列表进行修改，在每个魔术师名字中都加入字样"the Great".
# 调用函数 show_magicians()，确认魔术师列表确实变了。
def make_great(magicians, new_magicians):
    """
    循环打印列表每个元素
    加入字样
    并添加进空列表
    """
    while magicians:
        great = 'the Great ' + magicians.pop()
        new_magicians.append(great.title())
def show_magicians(new_magicians):
    """显示打印好的所有列表元素"""
    for magicians in new_magicians:
        print(magicians)
magicians = ['lee', 'jake', 'tom']
new_magicians = []
make_great(magicians, new_magicians)
show_magicians(new_magicians)
# 8-11 不变的魔术师：修改为完成 8-10 所编写的程序；
# 在调用函数 make_great() 时，向它传递魔术师列表副本。
# 由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用 show_magicians()，确认一个列表包含的是原来魔术师的名字；
# 而另一个列表则包含的是添加了"the Great"字样的魔术师名字。
def make_great(magicians, new_magicians):
    while magicians:
        great = 'the Gteat ' + magicians.pop()
        new_magicians.append(great.title())
def show_magicians(new_magicians):
    for magicians in new_magicians:
        print(magicians)
magicians = ['lee', 'jake', 'tom']
new_magicians = []
make_great(magicians[:], new_magicians)
show_magicians(new_magicians)
show_magicians(magicians)
