# # 1.写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
# def sum(*args):
#     count = 0
#     for i in args:
#         count = count+i
#     return count
# print(sum(1,2,3))
# # 2.看代码写结果
# def func():
#     return 1, 2, 3
# val = func()
# print(type(val) == tuple)
# print(type(val) == list)

##3.看代码写结果
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)

# a. 请将执行函数，并实现让args的值为 (1,2,3,4)
# def func(*args,**kwargs):
#     print(args)
# func(1,2,3,4)
# b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
# def func(*args,**kwargs):
#     print(args)
# func([1,2,3,4],[11,22,33])
# # c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func([11,22],33,k1 ='v1',k2='v2')
# # d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func(*{'武沛齐','金鑫','女神'})
# # e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func({'武沛齐','金鑫','女神'},[11,22,33])
# # f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'v1','k2':'v2'})

# 4.看代码写结果
def func(name,age=19,email='123@qq.com'):
    print(name,age,email)

# a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 结果：'alex'  19  '123@qq.com'

# b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 结果：'alex'  20  '123@qq.com'

# c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 结果：'alex',20,30

# d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 结果：alex 19 x@qq.com

# e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 结果：alex 99 x@qq.com

# f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 不能执行，关键字参数应该在位置参数后面
# g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# 不能执行，关键字参数应该在位置参数后面

# 5.看代码写结果
# def func(users,name):
# 	users.append(name)
#     return users
# result = func(['武沛齐','李杰'],'alex')
# print(result)
# 答案：['武沛齐','李杰','alex']

# # 6.看代码写结果
# def func(v1):
#     return v1* 2
# def bar(arg):
#     return "%s 是什么玩意？" %(arg,)
# val = func('你')
# data = bar(val)
# print(data)
# 结果：你你 是什么玩意

# # 7.看代码写结果
# def func(v1):
#     return v1* 2
#
# def bar(arg):
#     msg = "%s 是什么玩意？" %(arg,)
#     print(msg)
#
# val = func('你')
# data = bar(val)
# print(data)
# 结果：你你 是什么玩意？
# None

# # 8.看代码写结果
# v1 = '武沛齐'
# def func():
#     print(v1)
# func()
# v1 = '老男人'
# func()
# 结果：武沛齐
# 老男人

# # 9. 看代码写结果
# v1 = '武沛齐'
# def func():
#     v1 = '景女神'
#     def inner():
#         print(v1)
#     v1 = '肖大侠'
#     inner()
# func()
# v1 = '老男人'
# func()
# 结果：
# 肖大侠
# 肖大侠

# # 10.看代码写结果
# def func():
#     data = 2*2
#     return data
#
# new_name = func
# val = new_name()
# print(val)
# # 注意：函数类似于变量，func代指一块代码的内存地址。
# 结果：4

# # 11.看代码写结果【可选】
# def func():
#     data = 2*2
#     return data
#
# data_list = [func,func,func]
# for item in data_list:
#     v = item()
#     print(v)
# # 注意：函数类似于变量，func代指一块代码的内存地址。
# 结果：
# 4
# 4
# 4

# # 12.看代码写结果（函数可以做参数进行传递）【可选】
# def func(arg):
#     arg()
#
# def show():
#     print('show函数')
#
# func(show)
# # 结果：show函数
# # 13.写函数，接收n个数字，求这些参数数字的和。（动态传参）
# def sum(*args):
#     count = 0
#     for i in args:
#         count +=i
#     return count
# print(sum(1,2,3))
# # 14.读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#     print(a,b)
# c = test5(b,a)
# print(c)
# # 结果：
# # 20 10
# # None
# # 15.读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#     a=3
#     b=5
#     print(a,b)
# c = test5(b,a)
# print(c)
# # 结果:
# # 3 5
# # None
# # 16.传入函数中多个列表和字典, 如何将每个列表的每个元素依次添加到函数的动态参数args里面？如何将每个字典的所有键值对依次添加到kwargs里面？
# # args 用 *    kwargs 用  **
# def func(*args,**kwargs):
#     print(args,kwargs)
# func(*[0,1,2,3,4,5],**{'k1':'1','k2':'2'})
# 传值的时候打散，接收参数的时候聚合
# # 17.写函数, 接收两个数字参数, 将较小的数字返回.
# def bidaxiao(a,b):
#     return a if a<b else b
# print(bidaxiao(1,2))

# # 18.写函数, 接收一个参数(此参数类型必须是可迭代对象), 将可迭代对象的每个元素以’_’相连接, 形成新的字符串, 并返回.
# # 例如
# # 传入的可迭代对象为[1, '老男孩', '武sir']
# # 返回的结果为’1_老男孩_武sir’
# def pinjie(*args):
#     li = []
#     for i in args:
#         li.append(str(i))
#     s = '_'.join(li)
#     return s
# print(pinjie(*[1, '老男孩', '武sir']))

