# coding: GBK 
# 11-1:城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。
# 这个函数返回一个格式为 City, Country 的字符串。
# 11-2 人口数量：修改函数，使其包含第三个必不可少的形参 population。
# 返回一个格式为 City, Country - population xxx de 字符串。
# 修改函数，将形参 population 设置为可选的。
def city_and_country(city, country, population=''):
    """城市与国家名"""
    if population:
        full_show = city + ", " + country + "-" + population
    else:
        full_show = city + ", " + country
    return full_show.title()
