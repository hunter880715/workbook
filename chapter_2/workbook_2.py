# 3-4 嘉宾名单：创建一个嘉宾名单，至少包含三个人；
# 使用此列表打印消息，邀请这些人来与你共进晚餐。
guests = ["jin yong","liang yusheng","gu long","huang yi"]
print("兹邀请" + " " + guests[0].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[1].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[2].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[3].title() + " " + "先生参加今日晚宴。\n")
# 3-5 修改嘉宾名单：有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础；
# 在程序末尾添加一个 print 语句，指出哪位无法参加。
print(guests[2].title() + " " + "先生无法出席今日的宴会，甚为遗憾。\n")
# 修改嘉宾名单，将无法赴约的嘉宾姓名替换为新邀请的嘉宾姓名。
# 再次打印，向名单内每位嘉宾发出邀请。
guests[2] = "wen ruian"
print(guests)
print("\n兹邀请" + " " + guests[0].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[1].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[2].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[3].title() + " " + "先生参加今日晚宴。\n")
# 3-6 你敢找到一张更大的桌子，可以容纳更多嘉宾，再次添加三位嘉宾。
# 以先前完成的程序为基础，在程序末尾添加一条print语句，指出找到了一张更大的桌子。
mess = guests[0].title() + ',' + guests[1].title() + ','
mess_1=guests[2].title() + ',' + guests[3].title()
print(mess + mess_1 + "，先生们，我们找到了一张更大的桌子用以开展今晚的宴会。")
# 使用 insert() 将一位新嘉宾添加到名单开头。
# 使用 insert() 将另一位新嘉宾添加到名单中间。
# 使用 append() 将最后一位新嘉宾添加到名单末尾。
guests.insert(0,'yang guo')
guests.insert(3,'guo jing')
guests.append('huang rong')
print(guests)
# 3-9 指出多少嘉宾共进晚餐。
print("\n一共邀请了" + str(len(guests)) + "位嘉宾共聚晚宴。\n")
# 打印一系列消息，项名单中的每位嘉宾发出邀请。
print("\n兹邀请" + " " + guests[0].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[1].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[2].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[3].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[4].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[5].title() + " " + "先生参加今日晚宴。\n")
print("兹邀请" + " " + guests[6].title() + " " + "女士参加今日晚宴。\n")
# 3-7 缩减名单：刚得知新买的餐桌无法及时到达，因此只能邀请两位嘉宾。
# 以完成练习 3-6 时编写的程序为基础，在程序末尾打印一条只能邀请两位嘉宾的消息。
# 使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
# 每次弹出一位嘉宾，都打印一条消息，让嘉宾知悉歉意，无法共进晚餐。
print("各位先生与女士，因为自身原因此次宴会只能邀请两位嘉宾。\n")
a = guests.pop(0)
print(a.title() + " " + "先生，很抱歉今晚无法与您共进晚餐。\n")
b = guests.pop(0)
print(b.title() + " " + "先生，很抱歉今晚无法与您共进晚餐。\n")
c = guests.pop(0)
print(c.title() + " " + "先生，很抱歉今晚无法与您共进晚餐。\n")
d = guests.pop(1)
print(d.title() + " " + "先生，很抱歉今晚无法与您共进晚餐。\n")
e = guests.pop(1)
print(e.title() + " " + "先生，很抱歉今晚无法与您共进晚餐。\n")
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他们依然在受邀之列。
print(guests[0].title() + " " + "先生，您仍在今晚的宴会邀请当中。\n")
print(guests[1].title() + " " + "女士，您仍在今晚的宴会邀请当中。\n")
# 使用 del 将最后的两位嘉宾从名单中删除，让名单编程空的，并打印确认。
del guests[0]
del guests[0]
print(guests)
# 3-8 放眼世界：想出至少5个渴望去旅行的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按照字母排列的。
# 按原始排列顺序打印列表，不需要考虑是否整洁，只管打印原始 print 列表。
tours = ["spain","greenland","china","japan","italy"]
print(tours)
# 用 sorted() 按字母顺序打印列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使用 sorted() 按字母顺序相反的顺序打印列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
print(sorted(tours))
print(tours)
print(sorted(tours,reverse=True))
print(tours)
# 使用 reverse() 修改列表元素的排列顺序，打印该列表，核实排列顺序确实变了。
# 使用 reverse() 再次修改列表元素的排列顺序，打印并核实已恢复到原来的排列顺序。
# 使用 sort() 修改列表，按字母排列，并打印确定。
# 使用 sort() 再次修改列表，按字母相反顺序排列，并打印确定。
tours.reverse()
print(tours)
tours.reverse()
print(tours)
tours.sort()
print(tours)
tours.sort(reverse=True)
print(tours)
# 3-9 晚餐嘉宾：在 3-4~3-7 练习的程序之一中，使用 len() 打印一条消息指出邀请嘉宾人数。
# （答案见 line 33）
# 3-10 尝试使用各种函数：创建一个列表，本章所学的函数至少使用一次。
listings = []
listings.append("yellow river")
listings.insert(0,"taishan")
listings.insert(1,"great wall")
listings.append("fuji")
print(listings)
print(sorted(listings))
print(sorted(listings,reverse=True))
listings.reverse()
listings.reverse()
print(listings)
listings.sort(reverse=True)
listings.sort()
print(listings)
print("\n我已经去过" + str(len(listings)) + "个地方旅行了。\n")
great = listings.pop(1)
print("I have been to the" + " " + great.title() + ".\n")
print(listings)
fu = "fuji"
listings.remove(fu)
print("\nI have been to Mount" + " " + fu.title() + ".\n")
print(listings)
del listings[1]
del listings[0]
print(listings)
