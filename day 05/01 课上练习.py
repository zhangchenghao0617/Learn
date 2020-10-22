
# 字典的增删改查：
# dic = {'name': '太白', 'age': 18,}
# 增：
# 直接增加 有则改之，无则增加
# dic['sex'] = '男'
# dic['age'] = 23  # 改
# print(dic)
# setdefault  有则不变，无则增加
# dic.setdefault('hobby')
# dic.setdefault('hobby', '球类运动')
# dic.setdefault('age', 45)
# print(dic)

# 删
# pop 按照键删除键值对, 有返回值  ***
# 设置第二个参数则无论字典中有无此键都不会报错
# dic.pop('age')
# ret = dic.pop('age')
# ret = dic.pop('age','没有此键')
# print(ret)
# print(dic)

# clear  清空  **
# dic.clear()
# print(dic)

# del  **
# # del dic['age']
# del dic['age1']
# print(dic)


# 改
# dic['name'] = 'alex'
# print(dic)

# 查
# print(dic['hobby_list'])
# print(dic['hobby_list1'])

# get  ***
# l1 = dic.get('hobby_list')
# l1 = dic.get('hobby_list1','没有此键sb')  # 可以设置返回值
# print(l1)

# 三个特殊的
# keys() values() items()
# print(dic.keys(),type(dic.keys()))
# 可以转化成列表
# print(list(dic.keys()))
# for key in dic.keys():
#     print(key)
# for key in dic:
#     print(key)


# values()
# print(dic.values())
# print(list(dic.values()))
# for value in dic.values():
#     print(value)


# items()
# print(dic.items())
# for key,value in dic.items():
#     print(key,value)
# a,b = ('name', '太白')
# print(a,b)
# 面试题
# a = 18
# b = 12
# a,b = b,a
# # a,b = 12,18
# print(a,b)
# 练习题
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)
# dic.setdefault('k4','v4')
# print(dic)
# # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
# # 请在k3对应的值中追加一个元素 44，输出修改后的字典
# k3 = dic.get('k3','没有此键')
# print(k3)
# k3.append(44)
# print(dic)
# # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# k3 = dic.get('k3','没有此键')
# k3.insert(0,18)
# print(k3)
# print(dic)

# dic = {
#     'name':'汪峰',
#     'age': 48,
#     'wife': [{'name':'国际章','age':38}],
#     'children':{'girl_first': '小苹果','girl_second': '小怡','girl_three': '顶顶'}
# }
#
# # 1. 获取汪峰的名字。
# print(dic.get('name'))
# # 2.获取这个字典：{'name':'国际章','age':38}。
# print(dic.get('wife'))
# # 3. 获取汪峰妻子的名字。
# print(dic.get('wife')[0].get('name'))
# # 4. 获取汪峰的第三个孩子名字。
# print(dic.get('children','没有此键').get('girl_three'))

dic = {
 'name': ['alex',2,3,5],
 'job': 'teacher',
 'oldboy': {'alex':['python1','python2',100]}
 }
# # 1，将name对应的列表追加⼀个元素’wusir’。
# dic.get('name').append('wusir')
# print(dic)
# # 2，将name对应的列表中的alex⾸字⺟⼤写。
# list_name = dic.get('name')
# list_name[0] = 'Alex'
# print(dic)

# # 3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
# dic.get('oldboy').setdefault('⽼男孩','linux')
# print(dic)
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
dic.get('oldboy').get('alex').pop(1)
print(dic)


