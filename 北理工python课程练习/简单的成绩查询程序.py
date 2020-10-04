guess = eval(input('请输入分数：'))

if guess >= 90:
    grade = 'a'
elif guess >= 80:
    grade = 'b'
elif guess >= 60:
    grade = 'c'
else:
    grade = 'd'
print('成绩是: {}'.format(grade))
