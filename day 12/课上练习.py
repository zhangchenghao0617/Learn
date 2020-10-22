# def func():
#     li = []
#     for i in range(1,5001):
#         li.append(f'{i}号包子')
#     return li
# print(func())

# def func_iter():
#     for i in range(1,5001):
#         yield f'{i}号包子'
# ret = func_iter()
# for i in range(200):
#     print(next(ret))

# # 用列表推导式写出以下内容：
# # 1、10以内所有的数的平方
# print([i**2 for i in range(1, 11)])
# # 2、100以内所有的偶数
# print([i for i in range(0,101,2)])
# # 3、从python1期到python100期
# print([f'python{i}期' for i in range(1, 101)])

# # 1、三十以内可以被三整除的数。
# print([i for i in range(1, 31) if i % 3 == 0])
# # 2、过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
# print([i.upper() for i in l if len(i)>3])
# # 3、找到嵌套列表中名字含有两个‘e’的所有名字（有难度）
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# l = [i for li in names for i in li if i.count('e') ==2]
# print(l)
# 4、构建列表[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
# l = [i for i in range(2,11)] + list('JQKA')
# print(l)
# l = []
# for i in range(2,15):
#     if i==11:
#     if i==11:
#         i='J'
#     elif i == 12:
#         i = 'Q'
#     elif i == 13:
#         i = 'k'
#     elif i ==14:
#         i = 'A'
#     l.append(i)
# print(l)
