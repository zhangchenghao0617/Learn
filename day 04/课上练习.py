# li = [1, 3, 2, "a", 4, "b", 5,"c"]
#
# # 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# print(li[:3])
# # 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# print(li[3:6])
# # 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# print(li[1:6:2])
# # 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# print(li[-3::-2])

# li = ['张三','李四','王二','麻子']
# while 1:
#     name = input('请输入姓名:')
#     if name.upper() == 'Q': break
#     li.append(name)
# print(li)
#列表的创建
#方式1
#list = [1,张三,王二,李四]
#方式二
# l1 = list()
# l1 = list("asdfasdfasdf")
# print(l1)
#方式三
# 列表推导式 以后讲

# # 增删改查
# l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']

# # 增：
# # append:追加
# l1.append("张珊")
# print(l1)
# l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
# while 1:
#     name = input("请输入姓名:")
#     l1.append(name)
#     print(l1)
#     if name.upper() == "Q"
#         print("退出")
#         break
# # insert 插入
# l1.insert(0,"金坛")  #插入一个对象在索引之前
# print(l1)

#extend 迭代着追加

# l1.extend("abcd")
# print(l1)
#
# l1[2:] = ["张"]
# print(l1)

# l1 = [1, 2, 'taidai', [1, 'alex', 3,]]
# # 1, 将l1中的'taibai'变成大写并放回原处。
# l1[2] = l1[2].upper()
# print(l1)
# # 2，给小列表[1,'alex',3,]追加一个元素,'老男孩教育'。
# l1[3].append("老男孩教育")
# print(l1)
# # 3，将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
# l1[3][1] = l1[3][1] + "sb"
# print(l1)

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# # 将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
# 将列表中的数字3变成字符串"100"（用两种方式）。
# count = -1
# for i in lis:
#     count = count + 1
#     print(count)
#     if i == 3:
#         lis[count] = "100"
# print(lis)
# 将列表中的字符串"1"变成数字101（用两种方式）。
#
# l1 = [1, 2, 3,'alex', '太白', 2, 3, 4, 66,]
# for i in range(len(l1)):
#     print(i)
#




