# def max_size(num1,num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
# print(max_size(1,2))

# def meet(sex, age, skill, hight, weight):
#     print('进行筛选：性别：%s,年龄：%s，技能：%s，身高：%s,体重：%s' %(sex,age,skill,hight,weight))
#
# meet(sex = '男', age = 25, skill = 'python', hight = 175, weight = 100)

# def func(a,b):
#     return a+b
# print(func('asdf','123'))

def func(a):
    count = -1
    for i in a:
        count += 1
        if count < 2:
            return a[:2]
        else:
            return a

print(func([1,2,3,4]))