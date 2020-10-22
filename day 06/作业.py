# # 1.请用代码验证"name"是否在字典的键中？info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18',...100个键值对}
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
# li = info.get('name','没有此键')
# print(li)
# # 2.请用代码验证"alex"是否在字典的值中？
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
# li = []
# for i in info.values():
#     li.append(i)
# if 'alex' in li:
#     print('有')
# else:
#     print('没有')

# # 3.有如下
# v1 = {'武沛齐', '李杰', '太白', '景女神'}
# v2 = {'李杰', '景女神'}
#
# # - 请得到v1和v2的交集并输出
# print(v1 & v2)
# # - 请得到v1和v2的并集并输出
# print(v1 | v2)
# # - 请得到v1和v2的差集并输出
# print(v1 - v2)
# # - 请得到v2和v1的差集并输出
# print(v2 - v1)

# # 4.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
#
# list = []
# while 1:
#     add = input("请输入添加内容")
#     if add.upper() == 'N':
#         break
#     else:
#         list.append(add)
# print(list)
# # 5.循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
# set = set()
# while 1:
#     add = input("请输入添加内容:")
#     if add.upper() == 'N':
#         break
#     else:
#         set.add(add)
# print(set)
# # 6.写代码实现v1 = {'alex', '武sir', '肖大'},v2 = []
# #循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
# v1 = {'alex', '武sir', '肖大'}
# v2 = []
# while 1:
#     add = input('请输入内容：')
#     if add.upper() == 'N':
#         break
#     else:
#         if add in v1:
#             v2.append(add)
#         else:
#             v1.add(add)
# print(v1)
# print(v2)
# 7.
# 判断以下值那个能做字典的key ？那个能做集合的元素？
#
# - 1    能 能
# - -1   能 能
# - ""   能 能
# - None 能 能
# - [1, 2] 不能 不能
# - (1,)    能   能

# - {11, 22, 33, 4}  不能 不能
# - {'name': 'wupeiq', 'age': 18} 不能  不能

# 8. is 和 == 的区别？
#is 比较内存地址是否相等，==是比较值是否相等

# 9.
# type使用方式及作用？
#print(type(123)) 查询数据类型
# 10.
# # id的使用方式及作用？
# srt = 'a1231'
# print(id(srt))
#查询内存地址
# 11.
# 看代码写结果并解释原因
#

# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)
#
# True
# False

#值相等，但是内存地址不同
# 12.
# 看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)
#
# True
# True

#v1 和v2 是指向同一内存
# 13.
# 看代码写结果并解释原因

# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# v1['k1'] = 'wupeiqi'
# print(v2)

# {'k1': 'wupeiqi', 'k2': [1, 2, 3]}

#v1 和v2 是指向同一内存
# # 14.看代码写结果并解释原因
#
# v1 = '人生苦短，我用Python'
# v2 = [1, 2, 3, 4, v1]
# v1 = "人生苦短，用毛线Python"
# print(v2)
# # [1, 2, 3, 4, '人生苦短，我用Python']
#
# # 15.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
# info.append(9)
# print(userinfo)
# info = "题怎么这么多"
# print(userinfo)

# # 16.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)

# 17.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)
# ['闭嘴', 2, 3][['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3]]

# # 18.看代码写结果并解释原因
#
# info = [1, 2, 3]
# user_list = []
# user_list.append(info)
# for item in range(10):
#     user_list.append(info)
#     print(info)
# info[1] = "是谁说Python好学的？"
# print(user_list)

# 19.看代码写结果并解释原因
# data = {}
# for i in range(10):
#     data['user'] = i
# print(data)

# # 20.看代码写结果并解释原因
# data_list = []
# data = {}
# for i in range(10):
#     data['user'] = i
#     data_list.append(data)
#     print(data_list)
# print(data)

# 21.看代码写结果并解释原因
# data_list = []
# for i in range(10):
#     data = {}
#     data['user'] = i
#     data_list.append(data)
# print(data_list)

# 22.使用循环打印出一下效果：

# *
# **
# ***
# ****
# *****
#
# for i in range(6):
#     print(i * '*')

#
# -
# ****
# ***
# **
# *
#
# for i in range(4, 0, -1):
#     print(i * '*')

# -
#

# *
# ***
# *****
# *******
# *********
#
# for i in range(1, 10,2):
#     print(i * '*')

# 1. 敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.编程来完成敲七.给出⼀个任意的数字n.从1开始数.数到n结束.
# 把每个数字都放在列表中, 在数的过程中出现7或者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个'咣'
#
#
#
#
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
# num = input("请输入数字:").strip()
# li = []
# for i in range(1,int(num)+1):
#     if i % 7 == 0:
#         li.append("咣")
#     else:
#         li.append(i)
# print(li)


