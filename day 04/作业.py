# ## day04作业
#
# 1.写代码，有如下列表，按照要求实现每一个功能
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
# print(len(li))
# 列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# print(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,'Tony')
# print(li)
# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li.insert(1,'Kelly')
# print(li)

# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li.extend([1,"a",3,4,"heart"])
# print(li)
# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li.extend("qwert")
# print(li)

# 请删除列表中的元素"ritian",并输出添加后的列表
# li.remove("ritian")
# print(li)

# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# li.pop(1)
# print(li)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)

#2.写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# # 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# print(li[0:3])
# # 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# print(li[3:6])
# # 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# print(li[::2])
# # 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# print(li[1:-1:2])
# # 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# print(li[-1:-2:-1])
# # 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# print(li[-3:0:-2])

#3.写代码，有如下列表，按照要求实现每一个功能。
# lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
# 将列表中的数字3变成字符串"100"（用两种方式）。
# lis[3][2][1][1] = '100'
# print(lis)
# 将列表中的字符串"1"变成数字101（用两种方式）。
# lis[3][2][1][2] = 101
# print(lis)

#4.请用代码实现：
# li = ["alex", "wusir", "taibai"]
# # 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
#
# str = '_'.join(li)
# print(str)

# # 5.利用for循环和range打印出下面列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)

# # 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# li = []
# for i in range(0,101,2):
#     li.append(i)
# print(li)

# # 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
# li = []
# for i in range(0,51,3):
#     li.append(i)
# print(li)
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
# li = []
# for i in range(0,51):
#     if i%3 == 0:
#         li.append(i)
# print(li)
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# # 8.利用for循环和range从100~1，倒序打印。
# li = []
# for i in range(100,0,-1):
#     li.append(i)
# print(li)

# # 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
# li = []
# for i in range(100,9,-2):
#     li.append(i)
# print(li)
# for i in li:
#     if i % 4 != 0:
#         li.remove(i)
# print(li)

# # 10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
# li = []
# for i in range(1,31):
#     li.append(i)
# print(li)
# count = 0
# for i in li:
#     if i % 3 == 0:
#         li[count] = '*'
#     count += 1
# print(li)

# # 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "Abc ", "egon", " riTiAn", "WuSir", " aqc"]
# list_1 = []
# list_2 = []
# count = 0
# for i in li:
#     li[count] = i.strip()
#     count += 1
# print(li)
# for i in li:
#     if i.startswith("a") or i.startswith('A'):
#         list_1.append(i)
# for i in list_1:
#     if i.endswith('c'):
#         list_2.append(i)
# print(list_2)

# 12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的“*”（苍老师就替换成三个星），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]

# 13.有如下列表（选做题）
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7,
# 8
# "taibai"
# 5
# ritian
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in range(len(li)):
#     if isinstance(li[i],list):
#         list1 = li[i]
#         for a in range(len(list1)):
#             print(list1[a])
#     else:
#         print(li[i])
#
# def dayin(a):
#     for i in range(len(a)):
#         if isinstance(a[i], list):
#             dayin(a[i])
#         else:
#             print(a[i])
# dayin(li)

