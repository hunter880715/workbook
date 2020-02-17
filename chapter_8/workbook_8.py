# coding: GBK 
# 8-1 ��Ϣ����дһ����Ϊ display_message() �ĺ�����
# ��ӡһ�����ӣ�ָ��������ѧ����ʲô���������������ȷ����ʾ����Ϣ��ȷ����
def display_message():
    """������ѧ����"""
    print("��д��������ú�����\n")
display_message()
# 8-2 ϲ����ͼ�飺��дһ����Ϊ favorite_book �ĺ��������а���һ����Ϊ title ���βΡ�
# ���������ӡһ����Ϣ��������������������Ա�������������Ϊʵ�δ��ݸ�����
def favorite_book(title):
    """ϲ��������"""
    print("One of my favorite books is " + title.title() + ".\n")
favorite_book("golden slumber")
# 8-3 T������дһ����Ϊ make_shirt() �ĺ�����������һ�������Լ�Ҫӡ��T���ϵ�������
# �������Ӧ��ӡһ�����ӣ���Ҫ��˵��T���ĳ����������
# ʹ��λ��ʵ�ε����������������һ��T������ʹ�ùؼ���ʵ�����������������
def make_shirt(siza, typeface):
    """T���ĳ���������"""
    print("The T-shirt siza is " + siza + ";\n" + 
    "typeface: " + typeface + ".\n")
make_shirt("XXL", "I love Python")               # ʹ��λ��ʵ�ε��ú�����
make_shirt(siza='XXL', typeface="I love Python") # ʹ�ùؼ���ʵ�ε��ú�����
# 8-4 ���T�����޸ĺ��� make_shirt()��ʹ����Ĭ�ϵ����������ӡ��'I love Python'�Ĵ��T����
# ���������������������T����
# һ��ӡ��Ĭ�������Ĵ��T����һ��ӡ��Ĭ���������к�T���Լ�ӡ������������T����
def make_shirt(siza, typeface='I love Python'):
    """T���ĳ���������"""
    print("The T-shirt siza is " + siza + ";\n" +
    "typeface: " + typeface + ".\n")
make_shirt("XXXL")  # ���T��
make_shirt("L")     # �к�T��
make_shirt(siza="M", typeface="I love China") # ��������T��
# 8-5 ���У���дһ����Ϊ describe_city() �ĺ�����������һ�������Լ��ó��������Ĺ��ҡ�
# ���������ӡһ�����ӣ��� Reykjavik is in Iceland.
# �����ڴ洢���ҵ��β�ָ��Ĭ��ֵ��κ������ͬ�ĳ��е������������������������һ�����в�����������ҡ�
def describe_city(city, country="china"):
    """��������������"""
    print(city.title() + " is in " + country.title() + ".\n")
describe_city('chongqing')
describe_city('shanghai')
describe_city('landen', country='england')
# 8-6 ����������дһ����Ϊ city_country() �ĺ����������ܳ��е����Ƽ����������ҡ�
# �������Ӧ����һ����ʽ�������������ַ�����"Santiago,Chile"
# ����ʹ����������-���ҶԵ����������������ӡ���ķ���ֵ��
def city_country(city_name, country_name):
    """������������������"""
    full = city_name + "," + country_name
    return full.title()
mess = city_country("beijing", "china")
print(mess)
mess = city_country("tokiyo", "japan")
print(mess)
mess = city_country("new york", "america")
print(mess)
# 8-7 ר������дһ����Ϊ make_album() �ĺ�����������һ����������ר�����ֵ䡣
# �������Ӧ���ܸ��ֵ����ֺ�ר������������һ��������������Ϣ���ֵ䡣
# ʹ�������������������ʾ��ͬר�����ֵ䣬����ӡÿ�����ص�ֵ����ʵ�ֵ���ȷ�Ĵ洢��ר������Ϣ��
def make_album(singer_name, album_name):
    """��������ר����"""
    album = {'singer':singer_name, 'album':album_name}
    return album
album_1 = make_album('alan walker', 'faded')
print(album_1)
album_2 = make_album('taylor swfit', '1989')
print(album_2)
album_3 = make_album('katy perry', 'teenage dteam')
print(album_3)
# ������ make_album() ���һ����ѡ�βΣ��Ա��ܹ��洢ר���������ĸ�������
# ��������������ʱ�ƶ��˸��������ͽ����ֵ��ӵ���ʾר�����ֵ��С�
# ���������������������һ�ε�����ָ��ר�������ĸ�������
def make_album(singer_name, album_name, number=''):
    """���֡�ר���������Լ���������"""
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
# 8-8 �û���ר������ 8-7 ��ϰ��д�ĳ����У���дһ�� while ѭ�������û�����һ�����ֺ�ר������
# ��ȡ��Щ��Ϣ��ʹ�����������ú��� make_album()�������������ֵ��ӡ������
# ����� while ѭ���У����Ҫ�ṩ�˳�;����
def make_album(singer_name, album_name, number=''):
    """���֡�ר���������Լ���������"""
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
# 8-9 ħ��ʦ������һ������ħ��ʦ���ֵ��б������䴫�͸���Ϊ show_magicians() �ĺ�����
# ���������ӡ�б���ÿ��ħ��ʦ�����֡�
def show_magicians(names):
    """ħ��ʦ������"""
    for name in names:
        print(name.title())
magicians = ['lee', 'jake', 'tom']
show_magicians(magicians)
# 8-10 �˲����ħ��ʦ����Ϊ�����ϰ 8-9 ����д�ĳ����У���дһ����Ϊ make_great() �ĺ�����
# ��ħ��ʦ�б�����޸ģ���ÿ��ħ��ʦ�����ж���������"the Great".
# ���ú��� show_magicians()��ȷ��ħ��ʦ�б�ȷʵ���ˡ�
def make_great(magicians, new_magicians):
    """
    ѭ����ӡ�б�ÿ��Ԫ��
    ��������
    ����ӽ����б�
    """
    while magicians:
        great = 'the Great ' + magicians.pop()
        new_magicians.append(great.title())
def show_magicians(new_magicians):
    """��ʾ��ӡ�õ������б�Ԫ��"""
    for magicians in new_magicians:
        print(magicians)
magicians = ['lee', 'jake', 'tom']
new_magicians = []
make_great(magicians, new_magicians)
show_magicians(new_magicians)
# 8-11 �����ħ��ʦ���޸�Ϊ��� 8-10 ����д�ĳ���
# �ڵ��ú��� make_great() ʱ����������ħ��ʦ�б�����
# ���ڲ����޸�ԭʼ�б��뷵���޸ĺ���б�������洢����һ���б��С�
# �ֱ�ʹ���������б������� show_magicians()��ȷ��һ���б��������ԭ��ħ��ʦ�����֣�
# ����һ���б���������������"the Great"������ħ��ʦ���֡�
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
