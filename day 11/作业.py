# # 1、请写出下列代码的执行结果：﻿
# # 例一：
# def func1():
# 	print('in func1')
#
# def func2():
# 	print('in func2')
# ret = func1
# ret()
# ret1 = func2
# ret1()
# ret2 = ret
# ret3 = ret2
# ret2()
# ret3()
# # in func1
# # in func2
# # in func1
# # in func1

# # 例二：
# def func1():
# 	print('in func1')
# def func2():
# 	print('in func2')
# def func3(x,y):
# 	x()
# 	print('in func3')
# 	y()
# print(111)
# func3(func2,func1)
# print(222)
# # 111
# # in func2
# # in func3
# # in func1
# # 222

# 例三（选做题）：
# def func1():
# 	print('in func1')
# def func2(x):
# 	print('in func2')
# 	return x
# def func3(y):
# 	print('in func3')
# 	return y
# ret = func2(func1)  # ret = func1
# ret()               # func1()
# ret2 = func3(func2) # ret2 = func2
# ret3 = ret2(func1)  # ret3 = func2(func1)
# ret3()
# # in func2
# # in func1
# # in func3
# # in func2
# # in func1


# # 2、看代码写结果：
# (1)、
# def func(arg):
#     return arg.replace('苍老师', '***')
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
# run()
# #Alex的女朋友***和大家都是好朋友
# (2)、
# def func(arg):
#     return arg.replace('苍老师', '***')
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
# data = run()
# print(data)
# #Alex的女朋友***和大家都是好朋友
# #None


# # 3、看代码写结果：
# DATA_LIST = []
# def func(arg):
#     return DATA_LIST.insert(0, arg)
# data = func('绕不死你')
# print(data)
# print(DATA_LIST)
# # None
# # ['绕不死你']

# # 4、看代码写结果：
# def func():
#     print('你好呀')
#     return '好你妹呀'
# func_list = [func, func, func]
# for item in func_list:
#     val = item()
#     print(val)
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀

# # 5、看代码写结果：
# def func():
#     print('你好呀')
#     return '好你妹呀'
# func_list = [func, func, func]
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀

# # 6、看代码写结果：
# def func():
#     return '烧饼'
# def bar():
#     return '豆饼'
# def base(a1, a2):
#     return a1() + a2()
# result = base(func, bar)
# print(result)
# #烧饼豆饼

# # 7、看代码写结果：
# for item in range(10):
#     print(item)
# print(item)
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 9

# # 8、看代码写结果：
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func()
# #9

# # 9、看代码写结果：
# item = '老男孩'
# def func():
#     item = 'alex'
#     def inner():
#         print(item)
#     for item in range(10):
#         pass
#     inner()
# func()
# # 9

# # 10、看代码写结果：
# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
# print(func(1))
# print(func(2))
# print(func(3))
# # [1]
# # [1,2]
# # [1,2,3]

# # 11、看代码写结果：
# name = '太白'
# def func():
#     global name
#     name = '男神'
# print(name)
# func()
# print(name)
# # 太白
# # 男神

# # 12、看代码写结果：
# name = '太白'
# def func():
#     print(name)
# func()
# # 太白

# # 13、看代码写结果：
# name = '太白'
# def func():
#     print(name)
#     name = 'alex'
# func()
# # 报错

# # 14、看代码写结果：
# def func():
#     count = 1
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     print(count)
#     inner()
#     print(count)
# func()
# # 1
# # 2
# # 2

# # 15、看代码写结果：
# def extendList(val,list=[]):
# 	list.append(val)
# 	return list
# list1 = extendList(10)  #[10,a]
# list2 = extendList(123,[])# [123]
# list3 = extendList('a')# [10,a]
# print('list1=%s' %list1)
# print('list2=%s' %list2)
# print('list3=%s' %list3)
# # list1=[10, 'a']
# # list2=[123]
# # list3=[10, 'a']

# # 16、看代码写结果：
# def extendList(val,list=[]):
# 	list.append(val)
# 	return list
# print('list1=%s'% extendList(10)) #[10]
# print('list2=%s'% extendList(123,[])) #[123]
# print('list3=%s'% extendList('a')) #[10,a]
# # list1=[10]
# # list2=[123]
# # list3=[10, 'a']

# 17、用你的理解解释一下什么是可迭代对象，什么是迭代器。
# 可迭代对象: 更新迭代,重复的,循环的一个过程,更新迭代每次都有新的内容的叫可迭代对象
# 迭代器 : 内含有 __iter__ ,和 __next__ 方法的对象就是迭代器

# # 18、如何判断该对象是否是可迭代对象或者迭代器？
# with open('123.txt',encoding='utf-8',mode='w')as f:
#     print(('__iter__' in dir(f)) and ('__next__' in dir(f)))

# # 19、写代码：用while循环模拟for内部的循环机制（**面试题**）
# l1 = [11,22,33,44,55,66,77,88,99]
# obj = iter(l1)
# while 1:
#     try:
#         print(next(obj))
#     except StopIteration:
#         break

# # 20、写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}﻿
# # 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
# def min_max(*args):
#     return {'max':max(args),'min':min(args)}
# a = min_max(1,2,3,4,5)
# print(a)

# # 21、写函数，传入一个参数n，返回n的阶乘﻿
# # 例如:cal(7) 计算7*6*5*4*3*2*1
# def cal(*args):
#     a = 1
#     for i in range(1,args[0]+1):
#         a *= i
#         print(a)
#     return a
# cal(4)

# # 22、写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组(**选做题**)﻿
# # 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
# l1 = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
# l2 = []
#
# def func():
#     for i in l1:
#         lis1 = [("红心",i), ("草花",i),("黑桃",i),("方块",i)]
#         l2.extend(lis1)
#     return l2
# print(func())

# # 23、写代码完成99乘法表.(**选做题，面试题**)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={j*i} ',end = "  ")
#     print('\n')