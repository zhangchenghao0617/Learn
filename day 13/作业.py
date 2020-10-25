# 1.看代码分析结果
# func_list = []
# for i in range(10):
#     func_list.append(lambda: i)
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1, v2)

# 2.看代码分析结果

# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1, v2)


# 3.看代码分析结果

# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# for i in range(0, len(func_list)):
#     result = func_list[i](i)
#     print(result)

# 4.看代码写结果（面试题）：

# def func(name):
#     v = lambda x: x + name
#     return v
# v1 = func('太白')
# v2 = func('alex')
# v3 = v1('银角')
# v4 = v2('金角')
# print(v1, v2, v3, v4)

# 5.看代码写结果【面试题】

# result = []
# for i in range(10):
#     func = lambda: i  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)

# 6.看代码分析结果【面试题】
# def func(num):
#     def inner():
#         print(num)
#
#     return inner
#
#
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)

# 7.看代码写结果【新浪微博面试题】
# def func():
#     for num in range(10):
#         pass
#     v4 = [lambda: num + 10, lambda: num + 100, lambda: num + 100, ]
#     result1 = v4[1]()
#     result2 = v4[2]()
#     print(result1, result2)
# func()

# 8.请编写一个函数实现将IP地址转换成一个整数。【面试题，较难, 可以先做其他题】
# 如 10.3.9.12 转换规则为二进制：
#         10            00001010
#          3            00000011
#          9            00001001
#         12            00001100
# 再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？

# 完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
# 9.用map来处理字符串列表, 把列表中所有人都变成sb, 比方alex_sb
# name = [‘oldboy’, 'alex', 'wusir']
# name = ['oldboy', 'alex', 'wusir']
# ret = map(lambda x: x + '_sb', name)
# print(list(ret))

# 10.用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾

# l = [{'name': 'alex'}, {'name': 'y'}]
# l = [{'name': 'alex'}, {'name': 'y'}]
# ret = map(lambda x: x['name'] + '_sb', l)
# print(list(ret))

# 11.用filter来处理, 得到股票价格大于20的股票名字
# shares = {
#     'IBM': 36.6,
#     'Lenovo': 23.2,
#     'oldboy': 21.2,
#     'ocean': 10.2,
# }
# ret = filter(lambda x: shares[x] > 20, shares)
# print(list(ret))

# 12.有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0, ......]

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# ret = map(lambda x: x['shares'] * x['price'], portfolio)
# print(list(ret))

# 13.还是上面的字典，用filter过滤出单价大于100的股票。

# ret = filter(lambda x: x['price'] > 100, portfolio)
# print(list(ret))

# 14.有下列三种数据类型，
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')
# 写代码，最终得到的是（每个元祖第一个元素 > 2, 第三个 * 至少是4个。） [(3, 'wusir', ''), (4, '太白', '*******')]这样的数据。

# ​15.有如下数据类型(**实战题 **)：

# l1 = [{'sales_volumn': 0},
#
#       {'sales_volumn': 108},
#
#       {'sales_volumn': 337},
#
#       {'sales_volumn': 475},
#
#       {'sales_volumn': 396},
#
#       {'sales_volumn': 172},
#
#       {'sales_volumn': 9},
#
#       {'sales_volumn': 58},
#
#       {'sales_volumn': 272},
#
#       {'sales_volumn': 456},
#
#       {'sales_volumn': 440},
#
#       {'sales_volumn': 239}]

# ​将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。

# 16.求结果(**面试题 **)

# v = [lambda: x for x in range(10)]
#
# print(v)

# print(v[0])

# print(v[0]())

# 17.求结果(**面试题 **)

# v = (lambda: x for x in range(10))
# print(v)
# print(v[0])
# print(v[0]())
# print(next(v))
# print(next(v)())

# 18.map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])输出是什么? (** 面试题 **)

# 19.求结果：（ ** 面试题，比较难，先做其他题 **）
# def num():
#     return [lambda x: i * x for i in range(4)]
# print([m(2) for m in num()])

# 20.有一个数组[34，1, 2, 5, 6, 6, 5, 4，3, 3]请写一个函数，找出该数组中没有重复的数的总和（上面数据的么有重复的总和为1 + 2 = 3)(** 面试题 **)

# 21.写一个函数完成三次登陆功能：
# - 用户的用户名密码从一个文件register中取出。
# - register文件包含多个用户名，密码，用户名密码通过 | 隔开，每个人的用户名密码占用文件中一行。
# - 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# - 登陆成功返回True。

# 22.再写一个函数完成注册功能：
# - 用户输入用户名密码注册。
# - 注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# - 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# - 注册成功后，返回True, 否则返回False。

# 23.用完成一个员工信息表的增删功能（ ** 选做题，有时间做，没时间周末做 **）。
# 文件存储格式如下：
# id，name，age，phone，job
# 1, Alex, 22, 13651054608, IT
# 2, 太白, 23, 13304320533, Tearcher
# 3, nezha, 25, 1333235322, IT
# 现在要让你实现两个功能：
# 第一个功能是实现给文件增加数据，用户通过输入姓名，年龄，电话，工作，给原文件增加数据（增加的数据默认追加到原数据最后一行的下一行），但id要实现自增（id自增有些难度，id是不需要用户输入的但是必须按照顺序增加）。
# 第二个功能是实现给原文件删除数据，用户只需输入id，则将原文件对应的这一条数据删除（删除后下面的id不变，比如此时你输入1，则将第一条数据删除，但是下面所有数据的id值不变及太白，nezha的id不变）。