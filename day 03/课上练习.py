# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# # 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# print(li[0:3])
#
# # 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# print(li[3:6])
#
# # 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# print(li[1:6:2])
#
# # 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# print(li[-3:-8:-2])
#
# l = [1, 2, 'a']
# l.extend('太白a')
# print(l)
# l = ['太白', 'alex', 'WuSir', '女神']
# ret = l.pop(1)
# print(ret,l)

# a = [2,1,3,4,5]
# a.sort()
# a.rever se()#它也没有返回值，所以只能打印a
# print(a)

# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# #计算列表的长度并输出
#print(len(li))

# #列表中追加元素"seven",并输出添加后的列表
# li.append("seven")
# print(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,"Tony")
# print(li)

# #请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = "Kelly"
# print(li)

# # 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2=[1,"a",3,4,"heart"]
# print(li + l2)

# # 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# li.extend(s)
# print(li)

# # 请删除列表中的元素"ritian",并输出添加后的列表
# li.remove("ritian")
# print(li)
# # 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# li.pop(1)
# print(li)
# # 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)

# #  upper() lower() 练习
# username = input("请输入用户名：")
# password = input("请输入密码：")
# code = "qweR"
# print(code)
# your_code = input("请输入验证码：")
#
# if your_code.upper() == code.upper():
#     if username == "taibai" and password == "123456":
#         print("登录成功")
#     else:
#         print("账号或者密码错误")
# else:
#     print("验证码输入错误")
#
#format()
# #第一种用法：
# msg = '我叫{},今年{}，性别{}'.format('大壮',25,'男')
# #第二种用法：
# msg = '我叫{0},今年{1}，性别{2}，我依然叫{2}'.format('大壮',25,'男')
# #第三种用法：
# a = "大壮"
# msg = '我叫{name},今年{age}，性别{sex}，我依然叫{2}'.format(name = a,age = 25,sex = '男')









