# 1.整理今天笔记，课上代码最少敲3遍。

# 2.用列表推导式做下列小题
#
# 3.过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
# print([i.upper() for i in l if len(i)>3])

# 4.求(x, y)其中x是0 - 5之间的偶数，y是0 - 5之间的奇数组成的元祖列表
# print([(x,y) for x in range(6) for y in range(6) if x % 2 == 0 if y % 2 == 1])

# # 5.求M中3, 6, 9组成的列表
# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([i for l1 in M for i in l1 if i % 3 == 0])


# # 6.求出50以内能被3整除的数的平方，并放入到一个列表中。
# print([i**2 for i in range(51) if i % 3 == 0])
# # 7.构建一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# print([f'python{i}期' for i in range(1,11)])
# # 8.构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# print([(x, y) for x in range(6) for y in range(1, 7) if y-x == 1])
# print([(i, i + 1) for i in range(6)])
#
# # 9.构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# print([i for i in range(0,19,2)])
# # 10.有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# print([l1[i]+str(i) for i in range(4)])
# # 11.有以下数据类型：
# # x = {'name': 'alex',
# #      'Values': [{'timestamp': 1517991992.94, 'values': 100, },
# #                 {'timestamp': 1517992000.94, 'values': 200, },
# #                 {'timestamp': 1517992014.94, 'values': 300, },
# #                 {'timestamp': 1517992744.94, 'values': 350},
# #                 {'timestamp': 1517992800.94, 'values': 280}], }
# # 将上面的数据通过列表推导式转换成下面的类型：[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350],[1517992800.94, 280]]
# print([[i['timestamp'],i['values']] for i in x['Values']])


# 用列表完成笛卡尔积
#  什么是笛卡尔积？ 笛卡尔积就是一个列表，列表里面的元素是由输入的可迭代类型的元素对构成的元组，因此笛卡尔积列表的长度等于输入变量的长度的乘积。
# ​    a.构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# print([(x,y) for x in colors for y in sizes])
# n = [(colors[i],sizes[j])for i in range(len(colors)) for j in range(len(sizes))]
# print(n)

# # ​    b.构建一个列表, 列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
# n1 = ['spades','diamonds','clubs','hearts']
# list = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
# print([(x,y) for x in list for y in n1])


# 1.简述一下yield 与 yield from的区别。
# yield:是给next值
# yield from：是将列表变成迭代器返回
#
#
#
# # 2.看下面代码，能否对其简化？说说你简化后的优点？
# def chain(*iterables):
#     for it in iterables:
#         for i in it:
#             yield i
# g = chain('abc', (0, 1, 2))
# print(list(g))  # 将迭代器转化成列表
# def diedai(*args):
#     yield from [i for it in args for i in it ]
# g = diedai('abc', (0, 1, 2))
# print(list(g))

# 1.看代码求结果（ ** 面试题 **）：
# v = (i % 2 for i in range(10))
# print(v)  #一个生成器
# for i in range(5):
#     print(i) #0,1,2,3,4
# print(i)  #4

# 1.看代码求结果：（ ** 面试题 **）
def demo():
    for i in range(4):
        yield i
g = demo()
print(list(g))
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g1))
print(list(g2))

# 1.看代码求结果：（ ** 面试题 **）
# def add(n, i):
#     return n + i
# def test():
#     for i in range(4):
#         yield i
# g = test()
# for n in [1, 10]:
#     g = (add(n, i) for i in g)
# print(list(g))



